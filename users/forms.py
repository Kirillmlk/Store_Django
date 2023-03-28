from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'password'}))

    class Meta:
        model = User
        field = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'User Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password2')

