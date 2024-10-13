from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    company = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=20, choices=[
        ('Electronics', 'Electronics'),
        ('Sports', 'Sports'),
        ('Fashion', 'Fashion'),
        ('Home', 'Home'),
    ])

    def __str__(self):
        return self.name
