""" Import module from django """
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation, Customer


class CustomerForm(forms.ModelForm):

    """" Form for customer Phone Number placeholder """

    phone = forms.CharField(widget=forms.TextInput(
                            attrs={'placeholder': ('Please'
                                   'enter in +44 format')}))
    name = forms.CharField(required=False)

    class Meta:

        """ Add meta class for Name, Email and Date """

        model = Customer
        fields = ('name', 'email', 'phone')

    def clean_name(self, *args, **kwargs):
        """ Validate Name field  """

        name = self.cleaned_data.get("name")
        if not name.isalpha() and name.isnumeric():
            raise forms.ValidationError('Please enter valid name')
        if len(name) == '' or len(name) < 1:
            raise forms.ValidationError("Name field is required.")
        if '@' in name or '-' in name or '|' in name or '*' in name:
            raise forms.ValidationError(
                "Name should not have special characters.")
        return name


class ReservationForm(forms.ModelForm):

    """" Form for Reservation Date placeholder """

    date = forms.DateField()

    class Meta:

        """ Add meta class for Persons, Time, Date """

        model = Reservation
        fields = ['persons', 'time', 'date']


class CreateUserForm(UserCreationForm):

    """ create class for users form  """

    email = forms.EmailField()
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False,)

    class Meta:

        """ Add meta class for Register form  """

        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def clean_first_name(self, *args, **kwargs):
        """ Validate First name field  """

        f_name = self.cleaned_data.get("first_name")
        if not f_name.isalpha() and f_name.isnumeric():
            raise forms.ValidationError('Please enter valid first name')
        if len(f_name) == '' or len(f_name) < 1:
            raise forms.ValidationError("First name field is required.")
        if '@' in f_name or '-' in f_name or '|' in f_name or '*' in f_name:
            raise forms.ValidationError(
                "First name should not have special characters.")
        return f_name

    def clean_last_name(self, *args, **kwargs):
        """ Validate Last name field  """

        l_name = self.cleaned_data.get("last_name")
        if not l_name.isalpha() and l_name.isnumeric():
            raise forms.ValidationError('Please enter valid last name')
        if len(l_name) == '' or len(l_name) < 1:
            raise forms.ValidationError("Last name field is required.")
        if '@' in l_name or '-' in l_name or '|' in l_name or '*' in l_name:
            raise forms.ValidationError(
                "Last name should not have special characters.")

        return l_name
