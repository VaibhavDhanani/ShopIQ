# Generated by Django 5.1.2 on 2024-10-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.IntegerField(default=0)),
                ('company', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Sports', 'Sports'), ('Fashion', 'Fashion'), ('Home', 'Home')], max_length=20)),
            ],
        ),
    ]
