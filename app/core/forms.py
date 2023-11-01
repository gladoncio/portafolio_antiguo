from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.forms import ModelForm, fields, Form
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput




class UsuarioRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
    label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
    label='')
    class Meta:
        model = Usuario
        fields = ['username','email','password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'}),
                    'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
                    'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
                    }


        
class MyAuthForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['password'].label = False
