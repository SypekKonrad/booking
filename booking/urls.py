from django.urls import path, include
from django.contrib import admin
from booking import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.customer_list, name='customers'),
    # path('<int:vehicle_id>/vehicles/', views.vehicles, name='vehicles'),
    # path('<int:service_id>/services/', views.services, name='services'),
    #path('<int:customer_id>/customers/', views.customer_vehicle, name='vehicles'),
    path('details/', views.service_detail, name='details'),
    path('poll/', views.customer_poll, name='poll'),



]