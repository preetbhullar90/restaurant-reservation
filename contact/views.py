from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings



def send_email(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                name,
                message,
                email,
                ['admin@example.com']
                )

            messages.add_message(request, messages.SUCCESS, f" {name} ")

        return HttpResponseRedirect('/contact/')

    else:
        form = ContactForm()
        context = {
            'form' : form
        }
        return render(request, 'contact/contact.html', context)
