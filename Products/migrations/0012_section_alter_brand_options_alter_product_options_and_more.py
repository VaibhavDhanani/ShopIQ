# Generated by Django 5.1.2 on 2024-10-29 07:25

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Category", "0001_initial"),
        ("Products", "0011_alter_product_categories_delete_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(blank=True, unique=True)),
                (
                    "section_type",
                    models.CharField(
                        choices=[
                            ("REGULAR", "Regular Section"),
                            ("SEASONAL", "Seasonal Section"),
                            ("FESTIVAL", "Festival Special"),
                            ("PROMOTION", "Promotional Section"),
                        ],
                        default="REGULAR",
                        max_length=20,
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("is_active", models.BooleanField(default=True)),
                ("display_order", models.IntegerField(default=0)),
                ("start_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "background_color",
                    models.CharField(
                        blank=True, help_text="Hex color code", max_length=7
                    ),
                ),
            ],
            options={
                "ordering": ["display_order", "-created_at"],
            },
        ),
        migrations.AlterModelOptions(
            name="brand",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="brand",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="Products.brand",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(Decimal("0"))],
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(blank=True, max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="stock_quantity",
            field=models.PositiveIntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.CreateModel(
            name="SectionProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("display_order", models.IntegerField(default=0)),
                ("added_date", models.DateTimeField(auto_now_add=True)),
                (
                    "custom_title",
                    models.CharField(
                        blank=True,
                        help_text="Optional custom title for the product in this section",
                        max_length=100,
                    ),
                ),
                ("featured", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="section_products",
                        to="Products.product",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="section_products",
                        to="Products.section",
                    ),
                ),
            ],
            options={
                "ordering": ["display_order", "-added_date"],
            },
        ),
        migrations.AddField(
            model_name="product",
            name="sections",
            field=models.ManyToManyField(
                through="Products.SectionProduct", to="Products.section"
            ),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["name"], name="Products_pr_name_525943_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["created_at"], name="Products_pr_created_08b84c_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["price"], name="Products_pr_price_44d11c_idx"),
        ),
        migrations.AddIndex(
            model_name="sectionproduct",
            index=models.Index(
                fields=["section", "display_order"],
                name="Products_se_section_da790c_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="sectionproduct",
            index=models.Index(
                fields=["added_date"], name="Products_se_added_d_122377_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="sectionproduct",
            unique_together={("section", "product")},
        ),
    ]
