# Generated by Django 4.1.3 on 2022-12-26 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_customuser_type'),
        ('properties', '0023_alter_bedroomimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.agentuserprofile'),
        ),
    ]
