from django.shortcuts import render, redirect
from .forms import registerForm
from django.contrib import messages
# Create your views here.

def register(response):
    form = registerForm()
    
    if response.method == "POST":
        form = registerForm(response.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for'+ user)

    else:
        form = registerForm()
    return render(response, "register/register.html", {"form": form})
