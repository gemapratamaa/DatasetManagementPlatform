from django import forms
from django.forms import ModelForm

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput()
    )