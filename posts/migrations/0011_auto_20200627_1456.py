# Generated by Django 3.0.7 on 2020-06-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_merge_20200627_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='posts',
            field=models.ManyToManyField(blank=True, to='posts.Post'),
        ),
    ]
