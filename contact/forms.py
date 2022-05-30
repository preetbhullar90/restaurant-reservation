from django import forms


class ContactForm(forms.Form):
    """ Form for contact """
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

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
