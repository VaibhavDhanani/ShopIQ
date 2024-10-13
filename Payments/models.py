from django.db import models
from Orders.models import Order

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="payments"
    )
    payment_method = models.CharField(
        max_length=20, 
        choices=[
            ("CashOnDelivery", "Cash on Delivery"),
            ("UPI", "UPI"),
            ("Credit Card", "Credit Card")
        ]
    )
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id} - {self.payment_method}"
