# Generated by Django 4.1.6 on 2023-02-16 04:43

from django.db import migrations, models
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_property1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_profilename',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_profilepic',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_sentence',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_title',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(default=1, upload_to='update/', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.CharField(default=1, max_length=335),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
