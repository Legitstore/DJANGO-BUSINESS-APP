from django.forms import ModelForm
from .models import AddUserModel
from django import forms

class AddUserForm(ModelForm):
    class Meta:
        model = AddUserModel
        fields = '__all__'

        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'businessname': forms.TextInput(attrs={'class': 'form-control'}),
            'businessaddress': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }