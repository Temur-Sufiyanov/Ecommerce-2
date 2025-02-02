# Generated by Django 5.1.1 on 2024-10-26 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('product_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='product')),
                ('product_slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app.category')),
            ],
        ),
    ]
