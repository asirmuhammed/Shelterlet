# Generated by Django 4.1.2 on 2023-02-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_property_property_feature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_location',
            field=models.CharField(max_length=50),
        ),
    ]
