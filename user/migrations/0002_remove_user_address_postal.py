# Generated by Django 4.2.1 on 2023-06-02 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_address',
            name='postal',
        ),
    ]
