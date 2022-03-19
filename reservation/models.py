from django.db import models
from django.contrib.auth.models import User



time_choices = (
    ("07:00", "07:00"),
    ("08:00", "08:00"),
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    ("21:00", "21:00"),
    )




class Customer(models.Model):

    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=13, default='')
    owner = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return self.name


class Table(models.Model):

    table_name = models.CharField(max_length=20, default="New table", unique=True)
    max_no_people = models.IntegerField()

    def __str__(self):
        return self.table_name


