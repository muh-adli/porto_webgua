from django import forms

from .models import AuthUser

## Write your form here.
class registForm(forms.Form):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
            }
        )
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
            }
        )
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )
    password2 = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Retype Password',
            }
        )
    )

class loginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'id': 'username',
            }
        )
    )
    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'id': 'password',
            }
        )
    )