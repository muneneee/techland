# Generated by Django 3.0.7 on 2020-07-01 07:05

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
