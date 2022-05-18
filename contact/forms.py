from django import forms


class ContactForm(forms.Form):
    """ Form for contact """
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
