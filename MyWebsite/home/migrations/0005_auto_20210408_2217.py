# Generated by Django 3.1.7 on 2021-04-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210408_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Rejected', 'Rejected')], max_length=200, null=True),
        ),
    ]
