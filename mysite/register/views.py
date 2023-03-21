from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

# importing basic user form
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(response):
    #form = registerForm()
    #form = UserCreationForm()
    
    if response.method == "POST":
        #form = registerForm(response.POST)
        #form = UserCreationForm(response.POST)
        form = CustomUserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(response, f'Account created for {username}!')

    else:
        #form = registerForm()
        #form = UserCreationForm()
        form = CustomUserCreationForm()
    return render(response, "register/register.html", {"form": form})
