# Generated by Django 3.1.1 on 2020-10-10 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
        ('purchase', '0003_auto_20201010_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_order',
            name='user_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profile.userprofile'),
        ),
    ]
