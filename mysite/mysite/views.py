from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def welcome_view(request, context):
    return render(request, 'welcome.html', context)

def student_view(request, context):
    return render(request, 'student_dashboard.html', context)

def instructor_view(request, context):
    return render(request, 'instructor_dashboard.html', context)

@login_required
def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('login')

