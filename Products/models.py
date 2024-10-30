from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.utils.text import slugify
from Category.models import Category
from django.utils import timezone
from django.core.exceptions import ValidationError  
from django.conf import settings
    
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_products_count(self):
        return self.product_set.count()


class Section(models.Model):
    SECTION_TYPES = [
        ("REGULAR", "Regular Section"),
        ("SEASONAL", "Seasonal Section"),
        ("FESTIVAL", "Festival Special"),
        ("PROMOTION", "Promotional Section"),
    ]

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    section_type = models.CharField(
        max_length=20, choices=SECTION_TYPES, default="REGULAR"
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # banner_image = models.ImageField(
    #     upload_to="section_banners/", null=True, blank=True
    # )
    background_color = models.CharField(
        max_length=7, blank=True, help_text="Hex color code"
    )

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.name

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.name)

        if self.start_date and self.end_date:
            if self.start_date >= self.end_date:
                raise ValidationError("End date must be after start date")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    @property
    def is_active_period(self):
        now = timezone.now()
        if self.start_date and self.end_date:
            return self.start_date <= now <= self.end_date
        return True

    @property
    def is_visible(self):
        return self.is_active and self.is_active_period
    

    def get_active_products(self):
        return self.products.filter(
            sectionproduct__section=self, is_active=True
        ).order_by("sectionproduct__display_order", "-sectionproduct__added_date")


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=120)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal("0")), MaxValueValidator(Decimal("100"))],
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    categories = models.ManyToManyField(Category, related_name="products")
    sections = models.ManyToManyField(Section, through="SectionProduct")
    stock_quantity = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["price"]),
        ]

    def __str__(self):
        return self.name

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.name)

    def save(self, *args, **kwargs):
        # Generate a slug if it's not provided
        if not self.slug:
            potential_slug = slugify(self.name)
            unique_slug = potential_slug
            counter = 1

            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{potential_slug}-{counter}"
                counter += 1

            self.slug = unique_slug
        super().save(*args, **kwargs)

    @property
    def discounted_price(self):
        discount_factor = Decimal("1") - (self.discount_percentage / Decimal("100"))
        return (self.price * discount_factor).quantize(Decimal("0.01"))

    @property
    def is_in_stock(self):
        return self.stock_quantity > 0
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return f"{settings.MEDIA_URL}{self.image.name}"
        return None


class SectionProduct(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="section_products"
    )
    display_order = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)
    custom_title = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional custom title for the product in this section",
    )
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["display_order", "-added_date"]
        unique_together = ("section", "product")
        indexes = [
            models.Index(fields=["section", "display_order"]),
            models.Index(fields=["added_date"]),
        ]

    def __str__(self):
        return f"{self.section.name} - {self.product.name}"


class ActiveSectionManager(models.Manager):
    def get_queryset(self):
        now = timezone.now()
        return (
            super()
            .get_queryset()
            .filter(is_active=True, start_date__lte=now, end_date__gte=now)
        )
