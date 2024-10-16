from django.contrib import admin
from .models import Product, Category, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name","parent")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "discounted_price",
        "brand",
        "stock_quantity",
        "is_active",
    )
    list_editable = ("price", "stock_quantity", "is_active")
    search_fields = ("name", "description", "brand__name")
    list_filter = ("brand", "categories", "is_active")
    filter_horizontal = ("categories",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                    "brand",
                    "categories",
                )
            },
        ),
        ("Pricing", {"fields": ("price", "discount_percentage")}),
        ("Inventory", {"fields": ("stock_quantity", "is_active")}),
        (
            "Metadata",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
    prepopulated_fields = {"slug": ("name",)}

    def discounted_price(self, obj):
        return obj.discounted_price

    discounted_price.short_description = "Discounted Price"
