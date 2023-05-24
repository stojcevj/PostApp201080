# Generated by Django 4.0.3 on 2023-05-24 16:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PostApp', '0003_alter_post_post_created_alter_post_post_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 16, 36, 58, 673322)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_edited',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 16, 36, 58, 673391)),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(max_length=100)),
                ('comment_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostApp.post')),
                ('comment_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
