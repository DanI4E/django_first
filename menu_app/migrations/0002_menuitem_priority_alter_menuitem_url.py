# Generated by Django 5.1.2 on 2025-01-11 06:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='priority',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
