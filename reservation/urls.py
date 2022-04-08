from django.urls import path
from . import views


app_name = 'reservation'

urlpatterns = [

    path('', views.reserve_table, name='reserve_table'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_reservations/<pk>/', views.update_reservations,
         name='update_reservations'),
    path('delete_reservations/<pk>/', views.delete_reservations,
         name='delete_reservations'),
    path('<pk>/', views.customer_table, name='customer_table'),

]
