# Generated by Django 4.2 on 2023-05-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_delivery_fee_alter_cart_discount_price_mycard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Final Price'),
        ),
    ]
