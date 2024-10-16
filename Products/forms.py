from django import forms
from django.core.exceptions import ValidationError
from decimal import Decimal
from .models import Product, Brand, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "discount_percentage",
            "brand",
            "categories",
            "stock_quantity",
            "is_active",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "brand": forms.Select(attrs={"class": "form-select"}),
            "categories": forms.CheckboxSelectMultiple(),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

        def clean_discount_percentage(self):
            discount = self.cleaned_data["discount_percentage"]
            if discount < 0 or discount > 100:
                raise ValidationError(
                    "Discount percentage must be between in 0 and 100"
                )
            return discount

        def clean_price(self):
            price = self.cleaned_data["price"]
            if price <= Decimal("0.00"):
                raise ValidationError("Price must be greater than 0.")
            return price
