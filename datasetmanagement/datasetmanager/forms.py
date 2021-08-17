from django import forms
from django.forms import ModelForm

"""
class DatasetUploadForm(forms.Form):
    dataset_file = forms.FileField(
        label='Select a file',
    )
"""


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        required=True
    )
    password = forms.CharField(
        label='password',
        required=True,
        widget=forms.PasswordInput()
    )