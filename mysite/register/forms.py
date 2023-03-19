from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class registerForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
    
    class Meta:
        model = CustomUser
        fields = ('role','email', 'password1', 'password2')
