# Generated by Django 4.1.2 on 2023-02-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_property_property_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_tag',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
