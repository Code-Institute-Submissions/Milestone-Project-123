# Generated by Django 3.1.1 on 2020-09-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
