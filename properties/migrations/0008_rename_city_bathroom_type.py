# Generated by Django 4.1.3 on 2022-12-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_bathroom_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bathroom',
            old_name='city',
            new_name='type',
        ),
    ]
