# Generated by Django 4.1.3 on 2022-11-11 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
    ]
