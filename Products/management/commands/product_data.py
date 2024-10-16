from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps
from decimal import Decimal
from Products.models import Product, Category, Brand

class Command(BaseCommand):
    help = 'Add sample products data in database'

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write('Starting to populate sample data...')
            # Clear existing products if needed
            Product.objects.all().delete()
            Brand.objects.all().delete()
            
            # Populate the data
            self.populate_sample_data()
            
            self.stdout.write(self.style.SUCCESS('Successfully populated sample data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating data: {str(e)}'))

    def populate_sample_data(self):
        """Add sample data to the database."""

        # Fetch or create categories and brands
        electronics, _ = Category.objects.get_or_create(name="Electronics & Appliances")
        fashion, _ = Category.objects.get_or_create(name="Fashion & Apparel")
        grocery, _ = Category.objects.get_or_create(name="Grocery & Food Items")
        home, _ = Category.objects.get_or_create(name="Home & Furniture")

        apple, _ = Brand.objects.get_or_create(name="Apple")
        samsung, _ = Brand.objects.get_or_create(name="Samsung")
        sony, _ = Brand.objects.get_or_create(name="Sony")
        nike, _ = Brand.objects.get_or_create(name="Nike")
        adidas, _ = Brand.objects.get_or_create(name="Adidas")
        nestle, _ = Brand.objects.get_or_create(name="Nestlé")
        philips, _ = Brand.objects.get_or_create(name="Philips")

        # Electronics Products
        self.create_product(
            "iPhone 14 Pro", 
            "Latest Apple smartphone with A16 chip.", 
            999.99, 10, apple, 50, electronics
        )
        self.create_product(
            "Samsung Galaxy S23", 
            "Flagship Samsung smartphone with high-end camera.", 
            849.99, 5, samsung, 30, electronics
        )
        self.create_product(
            "Sony Bravia 55-inch TV", 
            "Ultra HD 4K Smart LED TV with HDR support.", 
            1199.99, 15, sony, 10, electronics
        )
        self.create_product(
            "Apple AirPods Pro", 
            "Noise-canceling wireless earbuds with spatial audio.", 
            249.99, 5, apple, 75, electronics
        )

        # Fashion Products
        self.create_product(
            "Nike Air Max Shoes", 
            "Comfortable running shoes with modern design.", 
            149.99, 20, nike, 100, fashion
        )
        self.create_product(
            "Adidas T-shirt", 
            "Stylish and breathable sportswear.", 
            39.99, 10, adidas, 200, fashion
        )

        # Grocery Products
        self.create_product(
            "Nestlé Coffee", 
            "Premium instant coffee for a quick caffeine boost.", 
            9.99, 0, nestle, 300, grocery
        )

        # Home Products
        self.create_product(
            "Philips Electric Kettle", 
            "Fast-boiling electric kettle with 1.7L capacity.", 
            49.99, 10, philips, 60, home
        )

    def create_product(self, name, description, price, discount, brand, stock, category):
        """Helper function to create a product and add it to a category."""
        product = Product.objects.create(
            name=name,
            description=description,
            price=Decimal(price),
            discount_percentage=Decimal(discount),
            brand=brand,
            stock_quantity=stock,
            is_active=True,
        )
        product.categories.add(category)
        self.stdout.write(self.style.SUCCESS(f'Added product: {name}'))