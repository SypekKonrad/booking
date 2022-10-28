from django.urls import path, include
from django.contrib import admin, auth
from booking import views, rest_views
#from django.contrib.auth import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.customer_list, name='customers'),
    # path('<int:vehicle_id>/vehicles/', views.vehicles, name='vehicles'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('<int:customer_id>/customers/', views.customer_vehicle, name='vehicles'),
    path('details/<int:vehicle_id>', views.service_detail, name='details'),
    path('poll/', views.customer_poll, name='poll'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/makes/', rest_views.MakeListView.as_view(), name='make-list'),
    path('api/models/', rest_views.MakeListView.as_view(), name='model-list'),


]