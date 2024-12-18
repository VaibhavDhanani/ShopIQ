# Generated by Django 5.1.2 on 2024-10-13 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccounts', '0002_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='addid',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='userid',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='UserAccounts.useraddress'),
        ),
    ]
