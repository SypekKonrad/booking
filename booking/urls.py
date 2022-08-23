from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:customer_id>/', views.customers, name='customers'),
    path('<int:vehicle_id>/', views.vehicles, name='vehicles'),
    path('<int:service_id>/', views.services, name='services'),

]