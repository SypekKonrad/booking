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
from job_management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('contactme/', contact_me, name='contact_me'),

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

    # urle do zlecen
    # todo usunac tego polla
    # path('poll/', customer_poll, name='poll'),
    # todo zmienic customer_poll2 na customer_poll
    path('poll/', customer_poll2, name='poll'),
    # todo customer list chyba tez do usuniecia
    # path('list/', customer_list, name='customers'),
    path('job_list/', job_list, name='job_list'),
    path('job_management/', job_management, name='job_management'),
    path('job_management/details/<int:id>', job_details, name='job_details'),
    path('job_assigned/<int:id>', job_assigned, name='job_assigned'),
    path('invoices/', invoice_management_panel, name='invoice_management_panel'),
    path('invoices/new/', invoice_gen, name='invoice_gen'),

    # path('job_assigned/invoices/invoice/new>', invoice_gen, name='invoice_gen'),



    # todo nie wiem czy to zostawie
    # path('details/<int:vehicle_id>', service_detail, name='details'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/makes/', MakeListView.as_view(), name='make-list'),
    path('api/models/', ModelListView.as_view(), name='model-list'),


]

