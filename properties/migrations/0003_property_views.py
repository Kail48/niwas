# Generated by Django 4.1.3 on 2022-12-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_videotour'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
