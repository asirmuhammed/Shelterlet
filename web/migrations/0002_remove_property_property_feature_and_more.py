# Generated by Django 4.1.2 on 2023-02-14 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_feature',
        ),
        migrations.RemoveField(
            model_name='property',
            name='property_tag',
        ),
    ]