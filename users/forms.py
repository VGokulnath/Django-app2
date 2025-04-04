from django import forms
from django.contrib.auth.models import User  #User model is created by django
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:       #inner class within a model that provides metadata to configure the model's behavior without altering its fields or methods.
        model = User
        fields = ['username','email','password1','password2']
