# Generated by Django 5.1.1 on 2024-10-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_clientmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmessage',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]