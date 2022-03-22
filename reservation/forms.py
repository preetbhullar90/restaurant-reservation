from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import Reservation, Customer

# class DateInput(forms.DateInput):
#      input_type = 'date'





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

    #date = forms.DateField(widget=DateInput)
    date = forms.DateField()


    class Meta:

        """ Add meta class for Persons, Time, Date """

        model = Reservation
        fields = ['persons', 'time', 'date']




class CreateUserForm(UserCreationForm):

    """ create class for users form  """

    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:

        """ Add meta class for Register form  """

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
