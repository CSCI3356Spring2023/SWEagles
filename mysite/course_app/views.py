from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import redirect
from course.models import AddCourseModel
from register.models import StudentUser
from .models import *
from django.http import HttpResponse
from mysite.utils import send_email

def course_app_view(response, course_id, current_user_id):


    data = AddCourseModel.objects.get(id=course_id)
    student = StudentUser.objects.get(id=current_user_id)
    #print(student.app_counter)
    if(student.app_counter > 4):
        return HttpResponse('you have applied to the maximum amount of applications!')

    Required = data.Cover_Letter
    Course_Name = data.Course_Name
    Course_Section = data.Section
    #print(Required)
    if(Required == 'required'):
        form = courseForm1()
        if response.POST:
            form = courseForm1(response.POST, response.FILES)
            if form.is_valid():

                application = form.save(commit=False)
                application.Course_Name = Course_Name
                application.Section = Course_Section
                student.app_counter+=1
                application.save()
                student.save()

                # Send successful application email
                message = "Hi "+student.first_name+",\n\n Thank you for applying to TA " + Course_Name+ "!"
                message += " You will be notified once your application is accepted or rejected." 
                message += " Feel free to keep applying to more positions, you can have up to five active applications at once."
                message += "\n\nBest,\n The SWEagles Team"
                subject = "Thank you for applying to TA " + Course_Name

                send_email(student.email, subject, message)                

                return redirect('student_landing_page')

        else:
            form = courseForm1()

        context = {
            'student' : student,
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
                student.app_counter+=1
                application.save()
                student.save()
                return redirect('student_landing_page')

        else:
            form = courseForm2()

        context = {
            'student' : student,
            'course' : data,
            'form' : form
        }

        return render(response, 'course_app_page.html', context)
