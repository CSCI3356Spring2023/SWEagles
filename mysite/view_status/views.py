from django.shortcuts import render, redirect
from course_app.models import courseApplicationAllRequired

from course_app.forms import courseForm1
from django.shortcuts import redirect
from course.models import AddCourseModel
from register.models import StudentUser
from .models import *
from django.http import HttpResponse

def view_status(response, course_name, student_username, application_status):


    context = {
            'student' : student_username,
            'course' : course_name,
            'application_status': application_status,
        }

    return render(response, 'view_status.html',  {'custom_attribute': context})

def update_hire_status(request, user_id, course_name):


    application = courseApplicationAllRequired.objects.get(Username=user_id, Course_Name=course_name)
    student = StudentUser.objects.get(Username=user_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status == 'accept':
            
            #update student status
            student.hire_status = "Hired"
            student.save()
            
            #update application status
            application.Application_Status = 'Accepted_by_both'
            application.save()
       
        elif status == 'reject':  
                   
            #update application status
            application.Application_Status = 'Rejected'
            application.save()
            


    context = {
        "course": application.Course_Name,
        "username": application.Username,
        "status": application.Application_Status
    }

    return render(request, 'view_status.html', {'custom_attribute': context})

