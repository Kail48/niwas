# Generated by Django 4.1.3 on 2022-12-26 09:25

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_tenantuserprofile_agentuserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentuserprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='tenantuserprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
