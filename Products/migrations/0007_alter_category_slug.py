# Generated by Django 5.1.2 on 2024-10-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_populate_category_slugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
