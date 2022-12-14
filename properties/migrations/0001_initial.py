# Generated by Django 4.1.3 on 2022-12-07 08:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_tenantuserprofile_agentuserprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('numbers', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(choices=[('SR', 'Single Room'), ('DR', 'Double Room'), ('1BHK', 'One bedroom, hall and Kitchen'), ('2BHK', 'Two bedroom, hall and Kitchen'), ('3BHK', 'Three bedroom, hall and Kitchen'), ('4BHK', 'four bedroom, hall and Kitchen')], default='1BHK', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(blank=True, null=True, upload_to='video/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parking', models.CharField(choices=[('NONE', 'NONE'), ('2W', 'Two Wheeler'), ('4W', 'Four Wheeler')], default='1BHK', max_length=5)),
                ('water', models.CharField(choices=[('NONE', 'NONE'), ('A', 'Anytime'), ('B', 'Boring Water'), ('T', 'Tank Water')], default='1BHK', max_length=5)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.agentuserprofile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.category')),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='image/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='BedroomImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='image/')),
                ('bedroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.bedroom')),
            ],
        ),
        migrations.AddField(
            model_name='bedroom',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property'),
        ),
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='image/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
    ]
