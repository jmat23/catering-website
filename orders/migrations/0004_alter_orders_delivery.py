# Generated by Django 4.0.4 on 2022-05-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orders_contact_alter_orders_cash_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivery',
            field=models.BooleanField(default=False),
        ),
    ]
