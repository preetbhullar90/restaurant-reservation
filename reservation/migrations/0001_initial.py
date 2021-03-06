# Generated by Django 3.2 on 2022-03-21 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=13)),
                ('owner', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(default='New table', max_length=20, unique=True)),
                ('max_no_people', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persons', models.IntegerField(choices=[(1, '1 person'), (2, '2 people'), (3, '3 people'), (4, '4 people')], default=1)),
                ('date', models.DateField(default='2022-01-28')),
                ('time', models.CharField(choices=[('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00')], default='12:00', max_length=10)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('rejected', 'rejected'), ('expired', 'expired')], default='pending', max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='reservation.customer')),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table_booked', to='reservation.table')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
