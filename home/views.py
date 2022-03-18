from django.shortcuts import render
from menu.models import Meals, Category
from aboutus.models import AboutUs, Why_Choose_Us, Chef
from contact.forms import ContactForm
from django.contrib import messages
#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='/reserve_table/login')
def home(request):
    about = AboutUs.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    meals = Meals.objects.all()
    categories = Category.objects.all()
    meal_list = Meals.objects.all()
    chef = Chef.objects.all()
    form = ContactForm()

    context = {
        'about' : about,
        'why_choose_us' : why_choose_us,
        'meals': meals,
        'categories': categories,
        'meal_list': meal_list,
        'chef' : chef,
        'form' : form,

    }

    return render(request,'home/home.html', context)