# Generated by Django 3.2 on 2023-01-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutRestaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='image',
            field=models.ImageField(default='image', upload_to='about_us/'),
        ),
    ]
