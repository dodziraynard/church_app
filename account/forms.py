from django import forms

from django.contrib.auth.models import User
from . models import Profile

class UserRegistrationForm(forms.ModelForm):
    password        = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_conf   = forms.CharField(label="Confirm Passowrd", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    username 		= forms.CharField(label="Username", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    class Meta:
        model = User
        fields = ['username', 'password', 'password_conf']

class UserLoginForm(forms.ModelForm):
    password    = forms.CharField(widget=forms.PasswordInput)
    username 	= forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "mobile",
            "image",
        ]