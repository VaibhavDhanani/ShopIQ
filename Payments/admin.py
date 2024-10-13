from django.contrib import admin
from Payments.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'payment_method', 'amount')
    search_fields = ('order__id',)
    list_filter = ('payment_method',)
