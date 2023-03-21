from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

def student_landing_page(request):
    return render(request, 'student_landing_page.html')