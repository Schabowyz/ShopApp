# Generated by Django 4.2.1 on 2023-06-08 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_item_current_price'),
        ('user', '0007_rename_user_address_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
        ),
    ]