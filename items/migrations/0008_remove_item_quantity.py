# Generated by Django 4.2.1 on 2023-06-24 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_delete_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]