# Generated by Django 4.1.6 on 2023-03-02 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_professionals'),
    ]

    operations = [
        migrations.CreateModel(
            name='agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=20)),
                ('agent_image', models.ImageField(upload_to='')),
                ('agent_post', models.CharField(max_length=20)),
            ],
        ),
    ]