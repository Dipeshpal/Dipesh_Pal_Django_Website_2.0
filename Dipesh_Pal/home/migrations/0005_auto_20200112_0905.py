# Generated by Django 2.2.6 on 2020-01-12 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200105_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('Created',)},
        ),
    ]