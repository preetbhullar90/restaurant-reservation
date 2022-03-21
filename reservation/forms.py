import email
from django import forms
from .models import Reservation, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings




class CustomerForm(forms.ModelForm):

    """" Form for customer Phone Number placeholder """

    phone = forms.CharField(widget=forms.TextInput(
    attrs={'placeholder': ('Please enter in +44 format')}))

    class Meta:

        """ Add meta class for Name, Email and Date """

        model = Customer
        fields = ('name', 'email', 'phone')



class ReservationForm(forms.ModelForm):

    """" Form for Reservation Date placeholder """

    date = forms.DateField(widget=forms.TextInput(
    attrs={'placeholder': ('2022-03-23')}))
    class Meta:

        """ Add meta class for Persons, Time, Date """

        model = Reservation
        fields = ['persons', 'time', 'date']
