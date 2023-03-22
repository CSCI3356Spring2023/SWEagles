from django.shortcuts import render, redirect
from .forms import courseForm
from django.http import HttpResponse

def course_app_view(response):
    form = courseForm()
    if response.POST:
        form = courseForm(response.POST, response.FILES)
        print(response.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Got it!")
    else:
        form = courseForm()
        
    return render(response, 'course_app_page.html', {'form': form})
