from django.shortcuts import render, redirect
from .forms import AddCourseForm
# Create your views here.

def add_course_view(request):
    form = AddCourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddCourseForm()

    return render(request, 'course_creation.html', {'form': form})    

  