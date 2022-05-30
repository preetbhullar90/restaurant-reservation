""" Import Django contrib, models and forms """
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Table, Customer, Reservation
from .forms import ReservationForm, CustomerForm, CreateUserForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def registerpage(request):
    """ Registration form for user """

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            html_message = render_to_string(
                'Reservation/register_email.html', {'name': first_name})
            plain_message = strip_tags(html_message)

            send_mail(
                'From: Mochi Restaurant',
                plain_message,
                'mochi_restaurant@site.com',
                [email],
                fail_silently=False,
                html_message=html_message,
            )
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            messages.success(
                request, f'{username} your account has been created ')

            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'Reservation/register.html', context)


def loginpage(request):
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


def logoutuser(request):
    """" Logout function for users """

    logout(request)
    return redirect('/')


def check_table_availabilty(customer_requested_time, customer_requested_date):
    """ check availability against Reservation model using customer input """

    # Check to see how many bookings exist at that time/date
    no_tables_booked = len(Reservation.objects.filter(
        time=customer_requested_time,
        date=customer_requested_date, status="confirmed"))
    # Return number of tables
    return no_tables_booked


def check_table_in_restaurant():
    """ Retrieves the number of tables in the table model """
    max_tables = len(Table.objects.all())
    return max_tables


@login_required(login_url='/reserve_table/login')
def create_order(request):
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

            # Send mail to the user when user send booking request
            from_email = request.user.email
            email = request.POST.get('email')
            html_message = render_to_string(
                'Reservation/create_booking_email.html',
                {'name': request.user.first_name})
            plain_message = strip_tags(html_message)

            send_mail(
                'From: Mochi Restaurant',
                plain_message,
                'mochi_restaurant@yahoo.com',
                [from_email, email],
                fail_silently=False,
                html_message=html_message,
            )
            date_formatted = datetime.datetime.strptime(
                customer_requested_date, "%m/%d/%Y")

            # Check to see how many bookings exist at that time/date
            tables_booked = check_table_availabilty(
                customer_requested_time, date_formatted)

            # Get the number of tables in the restaurant
            max_tables = check_table_in_restaurant()

            # Compare number of bookings to number of tables available
            if tables_booked >= max_tables:
                # If the number of tables is bigger than or equal to the
                # max number of tables in the restaurant stop form being
                # submitted

                messages.add_message(
                    request, messages.ERROR,
                    "Unfortunately we are fully booked at "
                    f"{customer_requested_time} on {customer_requested_date}.")
                return render(request, 'Reservation/create_reservation.html', {
                              'customer_form': customer_form,
                                       'form': form})

            else:

                venue = form.save(commit=False)
                venue.user = request.user
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

    return render(request, 'Reservation/create_reservation.html', {
                  'customer_form': customer_form, 'form': form})


@login_required(login_url='/reserve_table/login')
def reserve_table(request):
    """Create function for Reserve a Table """

    orders = request.user.reservation_set.all().order_by('-id')
    if len(orders) == 0:

        # if no reservations
        messages.add_message(request, messages.WARNING,
                             "Sorry, you don't have a any reserved table,"
                             "please reserve here.")

        return HttpResponseRedirect('/reserve_table/create_order/')
    else:
        customers = Customer.objects.all()
        today = datetime.datetime.now().date()
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

    view_booking = Reservation.objects.filter(id=pk)

    context = {
        'view_booking': view_booking,
    }
    return render(request, 'Reservation/view_reservation.html', context)


@login_required(login_url='/reserve_table/login')
def update_reservations(request, pk):
    """ funtion for update booking """

    order = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=order)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=order)
        if form.is_valid():
            order.status = 'pending'
            order.table = None
            order.customer = None
            form.save()
            # Send email to the user when user update the booking
            html_message = render_to_string(
                'Reservation/update_booking_email.html',
                {'name': request.user.first_name.capitalize()})
            plain_message = strip_tags(html_message)
            from_email = request.user.email

            send_mail(
                'From: Mochi Restaurant',
                plain_message,
                'mochi_restaurant@site.com',
                [from_email],
                fail_silently=False,
                html_message=html_message,
            )
            messages.add_message(request, messages.SUCCESS, "Thnx, your"
                                 " booking successfully updated.")

            return HttpResponseRedirect('/reserve_table/')

    context = {
        'form': form,
    }
    return render(request, 'Reservation/update_reservation.html', context)


@login_required(login_url='/reserve_table/login')
def delete_reservations(request, pk):
    """ Create funtion for delete single booking in booking list """

    order = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()

        # Send email to the user when user deleted the booking
        html_message = render_to_string(
            'Reservation/delete_booking_email.html',
            {'name': request.user.first_name.capitalize()})
        plain_message = strip_tags(html_message)
        from_email = request.user.email

        send_mail(
            'From: Mochi Restaurant',
            plain_message,
            'mochi_restaurant@site.com',
            [from_email],
            fail_silently=False,
            html_message=html_message,
        )
        messages.add_message(
            request, messages.SUCCESS,
            "Thanx, your booking successfully cancelled.")
        return redirect('/reserve_table/')
    context = {
        'item': order,
    }
    return render(request, 'Reservation/delete_reservation.html', context)
