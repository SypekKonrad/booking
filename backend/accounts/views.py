from django.shortcuts import render, redirect
from htmlmin.util import force_text

from .forms import *
from .token import *
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

from django.conf import settings
from django.contrib.auth import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'accounts/custom_password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/custom_password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/custom_password_reset_confirm.html'

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accounts/custom_password_change.html'
    success_url = reverse_lazy('password_change_done')

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/custom_password_change_done.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/custom_password_reset_complete.html'

class CustomLoginView(views.LoginView):
    authentication_form = CustomAuthenticationForm
    #template_name = 'accounts/login.html'

@login_required
def account_management(request):
    return render(request, 'accounts/management.html')


@login_required
def change_email(request):
    if request.method == 'POST':
        form = EmailChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            request.user.email = new_email
            request.user.save()
            return render(request, 'accounts/change_email_done.html')
    else:
        form = EmailChangeForm(user=request.user)

    return render(request, 'accounts/change_email.html', {'form': form})




def create_partner_account(request):
    if request.method == 'POST':
        form = CreatePartnerForm2(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(request.POST)
        if form.is_valid():
            #user = form.save()
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print('1')
            current_site = get_current_site(request)
            print('2')
            sender = settings.EMAIL_HOST_USER
            print('3')
            subject = 'Account activation'
            print('4')
            message = render_to_string('accounts/email_activation.txt', {
                'user':  form.cleaned_data.get('company_name'),
                'domain': current_site.domain,
                #'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            print('5')
            receiver = form.cleaned_data.get('email')
            print('6')
            send_mail(subject, message, sender, [receiver], fail_silently=False)
            print('7')


            return render(request, 'accounts/partner_account_registration_success.html', {'form': form})
    else:
        form = CreatePartnerForm2()
    return render(request, "accounts/create_partner_account.html", {'form': form})

def acc_activation(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
    return render(request, "accounts/partner_account_activation_success.html")


def partner_registration_successful(request):
    return render(request, "accounts/partner_account_registration_success.html")

