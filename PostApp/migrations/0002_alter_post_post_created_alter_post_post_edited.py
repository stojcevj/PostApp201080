# Generated by Django 4.0.3 on 2023-05-24 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_created',
            field=models.DateField(default=datetime.date(2023, 5, 24)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_edited',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 16, 10, 12, 761500)),
        ),
    ]
