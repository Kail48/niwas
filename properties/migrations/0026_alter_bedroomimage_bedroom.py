# Generated by Django 4.1.3 on 2023-01-11 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0025_property_reservations_bookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedroomimage',
            name='bedroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.bedroom'),
        ),
    ]