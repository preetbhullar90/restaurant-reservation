from django.contrib import admin
from .models import Customer, Table, Reservation



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'max_no_people')


@admin.register(Reservation)
class ReservationsAdmim(admin.ModelAdmin):
    list_filter = ('persons', 'status',)
    list_display = ('customer', 'persons', 'status',
                    'table', 'date', 'time')
