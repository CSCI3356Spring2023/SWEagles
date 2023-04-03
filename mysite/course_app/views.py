from django.shortcuts import render, redirect
from .forms import courseForm
from django.http import HttpResponse
from course.models import AddCourseModel
from .models import *

def course_app_view(response, course_id):

    data = AddCourseModel.objects.get(id=course_id)

    form = courseForm()
    Course_Name = response.POST.get('Course_Name')
    Course_Section = response.POST.get('Course_Section')
    if response.POST:
        form = courseForm(response.POST, response.FILES)
        if form.is_valid():

            application = form.save(commit=False)
            application.Course_Name = Course_Name
            application.Course_Section = Course_Section
            application.save()
            return HttpResponse(Course_Name)

    else:
        form = courseForm()

    context = {
        'course' : data,
        'form' : form
    }

    return render(response, 'course_app_page.html', context)
