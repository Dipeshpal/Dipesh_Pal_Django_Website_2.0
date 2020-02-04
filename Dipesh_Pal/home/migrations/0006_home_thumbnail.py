# Generated by Django 2.2.6 on 2020-01-25 12:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200112_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
