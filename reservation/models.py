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

    """ Model for customer """

    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=13, default='')
    owner = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return self.name


class Table(models.Model):

    """ Model for Table """

    table_name = models.CharField(
        max_length=20, default="New table", unique=True)
    max_no_people = models.IntegerField()

    def __str__(self):
        return self.table_name


class Reservation(models.Model):

    """ Model for Reservation """

    STATUS = (("pending", "pending"),
              ("confirmed", "confirmed"),
              ("rejected", "rejected"),
              ("expired", "expired"))

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer", null=True)

    table = models.ForeignKey(
        Table, on_delete=models.CASCADE,
        related_name="table_booked", null=True)

    guests_choices = ((1, "1 person"), (2, "2 people"),
                      (3, "3 people"), (4, "4 people"))

    persons = models.IntegerField(choices=guests_choices, default=1)

    date = models.DateField()

    time = models.CharField(
        max_length=10, choices=time_choices, default='12:00')

    status = models.CharField(
        max_length=200, null=True, choices=STATUS, default='pending')

    def __str__(self):
        return str(self.time)
