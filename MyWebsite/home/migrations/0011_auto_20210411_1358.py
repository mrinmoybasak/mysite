# Generated by Django 3.1.7 on 2021-04-11 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210411_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='asset_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='folio_No',
        ),
        migrations.RemoveField(
            model_name='product',
            name='investment_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='purchase_nav',
        ),
        migrations.RemoveField(
            model_name='product',
            name='purchase_redeem',
        ),
        migrations.RemoveField(
            model_name='product',
            name='purchase_value',
        ),
        migrations.RemoveField(
            model_name='product',
            name='units',
        ),
    ]
