from django.contrib.auth.forms import UserCreationForm
from .models import User

from django import forms
from django.contrib.auth.models import User
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
        
        

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': 'Password',
        'id': "id_password"
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
            })

        }

