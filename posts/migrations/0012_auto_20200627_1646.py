# Generated by Django 3.0.7 on 2020-06-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200627_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='categories',
            field=models.ManyToManyField(null=True, to='posts.Category'),
        ),
    ]
