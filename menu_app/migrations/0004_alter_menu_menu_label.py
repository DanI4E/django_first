# Generated by Django 5.1.2 on 2025-01-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0003_alter_menuitem_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_label',
            field=models.CharField(blank=True, max_length=256, unique=True),
        ),
    ]
