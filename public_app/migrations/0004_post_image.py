# Generated by Django 5.1.2 on 2024-11-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_app', '0003_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
