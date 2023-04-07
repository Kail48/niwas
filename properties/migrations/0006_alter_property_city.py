# Generated by Django 4.1.3 on 2022-12-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_property_address_property_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(choices=[('KTM', 'Kathmandu'), ('PK', 'Pokhara'), ('BT', 'Butwal'), ('BTM', 'Birtamode'), ('BTG', 'Biratnagar'), ('DH', 'Dharan')], default='KTM', max_length=5),
        ),
    ]