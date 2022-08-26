from django.urls import path, include
from django.contrib import admin
from booking import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:customer_id>/customers/', views.customer_list, name='customers'),
    # path('<int:vehicle_id>/vehicles/', views.vehicles, name='vehicles'),
    # path('<int:service_id>/services/', views.services, name='services'),
    path('<int:customer_id>/customers/', views.customer_vehicle, name='vehicles'),
    path('<int:customer_id>/customers/', views.service_detail, name='service'),
    path('/', views.customer_poll, name='poll'),



]