# Generated by Django 5.0.6 on 2024-05-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchanges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='currency_id',
            field=models.IntegerField(verbose_name='ID валюты'),
        ),
    ]
