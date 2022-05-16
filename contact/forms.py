from django import forms


class ContactForm(forms.Form):
    """ Form for contact """
    name = forms.CharField(widget=forms.TextInput(attrs={
           'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'placeholder': 'Your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={
              'placeholder': 'Your message'}))
