from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from django.contrib import messages
from mysite.utils import send_email

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

            # Send account creation email
            message = "Congratulations "+username+", your account with the TA System has been successuly created!"
            subject = "Boston College TA System Account Creation"
            send_email(form.cleaned_data.get('email'), subject, message)

            return redirect ('landing')

    else:
        #form = registerForm()
        #form = UserCreationForm()
        form = CustomUserCreationForm()
    return render(response, "register/register.html", {"form": form})
