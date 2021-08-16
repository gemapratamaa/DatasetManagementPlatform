from django import forms

class DatasetForm(forms.Form):
    dataset_file = forms.FileField(
        label='Select a file',
    )