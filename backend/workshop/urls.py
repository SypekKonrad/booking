"""workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView

from booking.views import *
from booking.rest_views import *
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', index, name='index'),

    path('register/partner/', create_partner_account, name='create_partner_account'),
    path('register/partner/success/', partner_registration_successful, name='partner_registration_successful'),
    path('activation/<str:uidb64>/<token>/', acc_activation, name='acc_activation'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('account/', account_management, name='account_management'),

    path('password/change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password/change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('email/change/', change_email, name='change_email'),
    # path('email/change/done/', change_email, name='change_email'),

    path('poll/', customer_poll, name='poll'),
    path('list/', customer_list, name='customers'),
    path('details/<int:vehicle_id>', service_detail, name='details'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/makes/', MakeListView.as_view(), name='make-list'),
    path('api/models/', ModelListView.as_view(), name='model-list'),

    # path('register/partner/failure/', create_partner_account, name='create_partner_account'),
    # path('activation/partner/failure/', partner_account_activation_1, name='partner_activation_1'),

    # path('create_accoount_1/', create_customer_account, name='create_customer_account'),
    # path('<int:customer_id>/customers/', views.customer_vehicle, name='vehicles'),
    # path('api/users/', rest_views.UsersListView.as_view(), name='user-list'),
    # path('<int:vehicle_id>/vehicles/', views.vehicles, name='vehicles'),
]

