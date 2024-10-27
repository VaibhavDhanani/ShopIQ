# Generated by Django 5.1.2 on 2024-10-13 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_method', models.CharField(choices=[('CashOnDelivery', 'Cash on Delivery'), ('UPI', 'UPI'), ('Credit Card', 'Credit Card')], max_length=20)),
                ('amount', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='Orders.order')),
            ],
        ),
    ]