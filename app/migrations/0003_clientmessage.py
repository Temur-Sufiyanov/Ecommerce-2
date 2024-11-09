# Generated by Django 5.1.1 on 2024-10-28 10:07

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_rating_count_product_total_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
    ]
