# Generated by Django 4.1.6 on 2023-02-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=20)),
                ('property_image', models.ImageField(upload_to='')),
                ('property_items', models.TextField()),
            ],
        ),
    ]
