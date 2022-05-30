""" All import libraries from django """
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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
                'Message: ' + message,
                'To' + email,
                recipient_list,
                fail_silently=False,
            )

            email = request.POST.get('email')
            html_message = render_to_string(
                'contact/contacts-mail.html', {'name': request.user.first_name})
            plain_message = strip_tags(html_message)

            send_mail(
                'From: Mochi Restaurant',
                plain_message,
                'mochi_restaurant@site.com',
                [email],
                fail_silently=False,
                html_message=html_message,
            )

            messages.add_message(request, messages.SUCCESS, f" {name} ")

        return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact/contact.html', context)
