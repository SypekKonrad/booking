from django import forms
from . models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
#from django.contrib.auth import forms
from django.utils.translation import gettext_lazy as _


class EmailChangeForm(forms.Form):
    old_email = forms.EmailField(label='Old Email', error_messages={'required': 'This field is required'})
    new_email = forms.EmailField(label='New Email', error_messages={'required': 'This field is required'})
    new_email_confirmation = forms.EmailField(label='Confirm New Email', error_messages={'required': 'This field is required'})

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
    def clean(self):
        cleaned_data = super().clean()
        old_email = cleaned_data.get('old_email')
        new_email = cleaned_data.get('new_email')
        new_email_confirmation = cleaned_data.get('new_email_confirmation')


        if new_email and new_email_confirmation and new_email != new_email_confirmation:
            raise forms.ValidationError("Provided e-mails can not be different.")

        elif old_email == new_email:
            raise forms.ValidationError("Provided e-mails have to different.")

        elif self.user.email != old_email:
            raise forms.ValidationError("Old e-mail is not valid.")


        return cleaned_data





class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("CUSTOM INACTIVE MESSAGE."),
    }


class CreatePartnerForm2(UserCreationForm):
    company_name = forms.CharField(label='company name', max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("the given username is already registered")
        return self.cleaned_data['username']

    def clean_company_name(self):
        if Partner.objects.filter(company_name=self.cleaned_data['company_name']).exists():
            raise forms.ValidationError("the given company is already registered")
        return self.cleaned_data['company_name']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        #user.is_active = False

        user.save()
        partner = Partner.objects.create(user=user, company_name=self.cleaned_data['company_name'])

        return user



# class LoginForm(AuthenticationForm):
#     def clean(self):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")
#
#         if username is not None and password:
#             self.user_cache = authenticate(
#                 self.request, username=username, password=password
#             )
#             if self.user_cache is None:
#                 raise self.get_invalid_login_error()
#             else:
#                 self.confirm_login_allowed(self.user_cache)
#
#         return self.cleaned_data
#
#     def confirm_login_allowed(self, user):
#
#         if not user.is_active:
#             raise ValidationError(
#                 self.error_messages["inactive"],
#                 code="inactive",
#             )
    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #
    #     self.user_cache = authenticate(self.request, username=username, password=password)
    #
    #     if not self.user_cache.is_active:
    #         raise forms.ValidationError("This account is inactive.")
    #
    #     if username is not None and password:
    #
    #         if self.user_cache is None:
    #             raise forms.ValidationError("Invalid username and/or password.")
    #
    #         # Check if the user is active
    #
    #
    #     return self.cleaned_data


