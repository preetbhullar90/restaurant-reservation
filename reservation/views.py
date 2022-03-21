from email import message
from django.shortcuts import render, redirect
from django.http import  HttpResponse,HttpResponseRedirect
from .models import *
from .forms import ReservationForm, CustomerForm, CreateUserForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Table, Customer, Reservation
from django.conf import settings
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout



def registerPage(request):

    """ Registration form for user """

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            messages.success(request, 'Account has been created ')

            return redirect('/')

    context = {
        'form' : form,
    }
    return render(request, 'Reservation/register.html', context)


#@unauthenticated_user
def loginPage(request):

    """ Login function for user  """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password incorrect')

    context = {}
    return render(request, 'Reservation/login.html', context)




def logoutUser(request):

    """" Logout function for users """

    logout(request)
    return redirect('/')


def check_availabilty(customer_requested_time, customer_requested_date):
    """ check availability against Reservation model using customer input """

    # Check to see how many bookings exist at that time/date
    no_tables_booked = len(Reservation.objects.filter(
        time=customer_requested_time,
        date=customer_requested_date, status="confirmed"))

    # Return number of tables
    return no_tables_booked

def get_tables_info():
    """ Retrieves the number of tables in the table model """
    max_tables = len(Table.objects.all())

    return max_tables








@login_required(login_url='/reserve_table/login')
#@allowed_users(allowed_roles=['customer'])
def create_order(request, User=User, *args, **kwargs):

    """Create function for get Reservation form """

    form = ReservationForm()
    customer_form = CustomerForm()
    if request.method == 'POST':
        # Get post data from forms
        customer_form = CustomerForm(data=request.POST)
        form = ReservationForm(data=request.POST)

        if customer_form.is_valid() and form.is_valid():
            # Retreive information from forms
            customer_requested_date = request.POST.get('date')
            customer_requested_time = request.POST.get('time')
            customer_requested_guests = request.POST.get('persons')
            customer_name = request.POST.get('name')

            # Convert date in to format required by django
            date_formatted = datetime.strptime(customer_requested_date,'%Y-%m-%d')


            # Check to see how many bookings exist at that time/date
            tables_booked = check_availabilty(
                customer_requested_time, date_formatted)

            # Get the number of tables in the restaurant
            max_tables = get_tables_info()

            # Compare number of bookings to number of tables available
            if tables_booked >= max_tables:
                """ If the number of tables is bigger than or equal to the
                max number of tables in the restaurant stop form being
                submitted
                """
                messages.add_message(
                    request, messages.ERROR,
                    "Unfortunately we are fully booked at "
                    f"{customer_requested_time} on {customer_requested_date}.")

                #return HttpResponseRedirect('/reserve_table/create_order/')
                return render(request, 'Reservation/create_reservation.html',
                                {'customer_form': customer_form,
                                 'form': form})

            else:

                    venue = form.save(commit=False)
                    venue.user= request.user
                    venue.save()
                    customer_form.save()
                    messages.add_message(
                            request, messages.SUCCESS,
                            f"Thank you {customer_name}, your enquiry for "
                            f"{customer_requested_guests} people at "
                            f"{customer_requested_time} on "
                            f"{customer_requested_date} has been sent.")

                    # Return blank forms so the same enquiry isn't sent twice.

                    return HttpResponseRedirect('/reserve_table/create_order/')

    return render(request, 'Reservation/create_reservation.html',
                    {'customer_form': customer_form,
                    'form': form})



@login_required(login_url='/reserve_table/login')
def reserve_table(request):
    """Create function for Reserve a Table """

    orders = request.user.reservation_set.all().order_by('-id')
    if len(orders) == 0:

        # if no reservations
        messages.add_message(
                        request, messages.WARNING,
                        f"Sorry, you don't have a any reserved table, please reserve here.")

        return HttpResponseRedirect('/reserve_table/create_order/')
    else:
        customers = Customer.objects.all()
        today = datetime.now().date()
        for reservation in orders:
            if reservation.date < today:
                reservation.status = 'expired'

        context = {
            'orders': orders,
            'customers': customers,
        }

        return render(request, 'Reservation/reservation.html', context)


@login_required(login_url='/reserve_table/login')
def customer_table(request, pk):

    """ Function for get customer id """

    pp = Reservation.objects.filter(id=pk)

    context = {
        'pp' : pp,
        }
    return render(request, 'Reservation/view_reservation.html', context)

@login_required(login_url='/reserve_table/login')
def update_order(request, pk):

    """ funtion for update booking """

    order = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=order)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, f'Thnx, your booking successfully updated.')

            return HttpResponseRedirect('/reserve_table/')

    context = {
        'form' : form,
    }
    return render(request, 'Reservation/update_reservation.html', context)


@login_required(login_url='/reserve_table/login')
def delete_order(request, pk):

    """ Create funtion for delete single booking in booking list """

    order = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        messages.add_message(
                            request, messages.SUCCESS,
                            f"Thanx, your booking successfully cancelled.")
        return redirect('/reserve_table/')
    context = {
        'item' : order,
    }
    return render(request, 'Reservation/delete_reservation.html', context)