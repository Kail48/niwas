# Generated by Django 4.1.3 on 2022-12-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_alter_videotour_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('OS', 'On sale'), ('S', 'Sold')], default='OS', max_length=5),
        ),
    ]