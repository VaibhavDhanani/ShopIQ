from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("type", "admin")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, name, password, **extra_fields)


class UserAddress(models.Model):
    id = models.AutoField(primary_key=True)
    street_no = models.CharField(max_length=10)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.street_no}, {self.street_name}, {self.city}"

    class Meta:
        verbose_name_plural = "User Addresses"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ("customer", "Customer"),
        ("seller", "Seller"),
        ("admin", "Admin"),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
        regex=r"^\d{10}$",
        message="Phone number must be entered as exactly 10 digits.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True
    )
    address = models.ForeignKey(
        UserAddress,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    business_registration_number = models.CharField(
        max_length=50, blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.type})"

    def save(self, *args, **kwargs):
        if self.type == "admin":
            self.is_staff = True
        super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.type == "admin"

    @property
    def is_seller(self):
        return self.type == "seller"

    @property
    def is_customer(self):
        return self.type == "customer"
