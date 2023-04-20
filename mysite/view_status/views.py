from django.shortcuts import render, redirect

from course_app.forms import courseForm1
from django.shortcuts import redirect
from course.models import AddCourseModel
from register.models import StudentUser
from .models import *
from django.http import HttpResponse

def view_status(response, course_name, student_username):


    context = {
            'student' : student_username,
            'course' : course_name,
        }

    return render(response, 'view_status.html',  {'custom_attribute': context})
