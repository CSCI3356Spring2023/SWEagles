from django.shortcuts import render
from .forms import registerForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = registerForm(response.POST)
        if form.is_valid():
            form.save()

    else:
        form = registerForm()
    return render(response, "register/register.html", {"form": form})
