# Generated by Django 2.2.6 on 2020-01-25 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_home_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='thumbnail',
        ),
    ]