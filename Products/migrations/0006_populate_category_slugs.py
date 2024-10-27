from django.db import migrations
from django.utils.text import slugify

def populate_category_slugs(apps, schema_editor):
    Category = apps.get_model('Products', 'Category')
    for category in Category.objects.all():
        if not category.slug:
            category.slug = slugify(category.name)
            category.save()

class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_remove_category_parent_category_slug_product_slug_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_category_slugs),
    ]