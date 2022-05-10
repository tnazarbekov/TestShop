from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserAuthentication(AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput()


class RegisterForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    message = forms.CharField(max_length=1000)
