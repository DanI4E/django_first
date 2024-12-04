from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)