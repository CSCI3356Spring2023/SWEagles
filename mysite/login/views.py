from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import CustomUserBackend


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUserBackend.authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            messages.info(request, f"You are {user.role}")
            user_info = request.user
            context = {'custom_attribute': {user.role}, 'username': username}
            return render(request, 'welcome.html', context)
        else:
            error_message = "Invalid email or password"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
