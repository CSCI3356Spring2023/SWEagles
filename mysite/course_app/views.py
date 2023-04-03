from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from course.models import AddCourseModel
from .models import *

def course_app_view(response, course_id):

    data = AddCourseModel.objects.get(id=course_id)

    Required = data.Cover_Letter
    Course_Name = data.Course_Name
    Course_Section = data.Section
    print(Required)
    if(Required == 'required'):
        form = courseForm1()
        if response.POST:
            form = courseForm1(response.POST, response.FILES)
            if form.is_valid():

                application = form.save(commit=False)
                application.Course_Name = Course_Name
                application.Section = Course_Section
                application.save()
                return HttpResponse(Course_Name)

        else:
            form = courseForm1()

        context = {
            'course' : data,
            'form' : form
        }

        return render(response, 'course_app_page.html', context)

    else:
        form = courseForm2()
        if response.POST:
            form = courseForm2(response.POST, response.FILES)
            if form.is_valid():

                application = form.save(commit=False)
                application.Course_Name = Course_Name
                application.Section = Course_Section
                application.save()
                return HttpResponse(Course_Name)

        else:
            form = courseForm2()

        context = {
            'course' : data,
            'form' : form
        }

        return render(response, 'course_app_page.html', context)
