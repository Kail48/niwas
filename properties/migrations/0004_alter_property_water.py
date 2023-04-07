# Generated by Django 4.1.3 on 2022-12-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_property_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='water',
            field=models.CharField(choices=[('NONE', 'NONE'), ('A', 'Anytime'), ('B', 'Boring Water'), ('T', 'Tank Water')], default='NONE', max_length=5),
        ),
    ]
