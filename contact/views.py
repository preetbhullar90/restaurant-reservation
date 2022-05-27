""" All import libraries from django """
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def send_email(request):

    """ Email sending form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(


                'From: ' + name,
                message,
                email,
                recipient_list,

                )
            messages.add_message(request, messages.SUCCESS, f" {name} ")

        return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact/contact.html', context)
