# Generated by Django 2.1.7 on 2019-02-20 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
