# Generated by Django 4.1.6 on 2023-03-03 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_workingwithshelterlet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='workingwithshelterlet',
            new_name='services',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='workingwithshelterlet_id',
            new_name='services_id',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='workingwithshelterlet_sentence',
            new_name='services_sentence',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='workingwithshelterlet_title',
            new_name='services_title',
        ),
    ]
