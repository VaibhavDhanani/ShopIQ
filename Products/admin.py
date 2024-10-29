from django.contrib import admin
from .models import *


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


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "section_type",
        "is_active",
        "display_order",
        "start_date",
        "end_date",
        "is_visible",
    )
    list_filter = ("section_type", "is_active", "start_date", "end_date")
    search_fields = ("name", "description")
    ordering = ("display_order", "-created_at")
    prepopulated_fields = {"slug": ("name",)}

    readonly_fields = ("created_at", "updated_at", "is_visible")

    def is_visible(self, obj):
        return obj.is_visible

    is_visible.boolean = True


@admin.register(SectionProduct)
class SectionProductAdmin(admin.ModelAdmin):
    list_display = ("section", "product", "display_order", "added_date", "featured")
    list_filter = ("section", "featured")
    search_fields = ("section__name", "product__name")
    ordering = ("display_order", "-added_date")
    autocomplete_fields = ("section", "product")
