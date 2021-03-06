# Generated by Django 3.1.7 on 2021-04-08 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_name', models.CharField(max_length=200, null=True)),
                ('asset_type', models.CharField(choices=[('Equity', 'Equity'), ('Debt', 'Debt'), ('Liquid ', 'liquid'), ('Others', 'Others')], max_length=200, null=True)),
                ('folio_No', models.CharField(max_length=200, null=True)),
                ('investment_date', models.DateField(null=True)),
                ('units', models.FloatField(null=True)),
                ('purchase_nav', models.IntegerField(null=True)),
                ('purchase_value', models.IntegerField(null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.product')),
            ],
        ),
    ]
