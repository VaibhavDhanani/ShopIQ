from django.db import models
from UserAccounts.models import CustomUser
from Products.models import Product

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=20, 
        choices=[
            ("Pending", "Pending"),
            ("Canceled", "Canceled"),
            ("Completed", "Completed"),
            ("Initiated", "Initiated")
        ], 
        default="Initiated"
    )

    def __str__(self):
        return f"OrderItem {self.id}: {self.quantity} x {self.product.name} (Order {self.order.id})"
