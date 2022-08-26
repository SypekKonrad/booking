from django import forms
from . models import post

class EmailForm(forms.Form):
    email = forms.Emailfield()
    model = Post
