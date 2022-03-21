from django.urls import path
from . import views


app_name = 'reservation'

urlpatterns = [

    path('', views.reserve_table, name='reserve_table'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<pk>/', views.update_order, name='update_order'),
    path('delete_order/<pk>/', views.delete_order, name='delete_order'),
    path('<pk>/', views.customer_table, name='customer_table'),

]