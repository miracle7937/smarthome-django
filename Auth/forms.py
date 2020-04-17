
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User






class CreateUserForm(UserCreationForm):
   
    email = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'name': "email", 'id': "text1", 'type': "email", 'value': "", 'placeholder': "Email"
        }
    ))
    password1 = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'name': "Password1", 'id': "muInput", 'type': "Password", 'value': "", 'placeholder': "Password"
        }
    )) 

    password2 = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'name': "Password2", 'id': "muInput", 'type': "Password", 'value': "", 'placeholder': "Confirm Password"
        }
    ))
  
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'name': "username", 'id': "text1", 'type': "text", 'value': "", 'placeholder': "User Name"
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

