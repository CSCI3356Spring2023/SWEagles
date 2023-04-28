from django.shortcuts import render, redirect
from .forms import *
from course.models import AddCourseModel
from register.models import StudentUser
from .models import *
from django.http import HttpResponse

def course_app_view(response, course_id, current_user_id):


    data = AddCourseModel.objects.get(id=course_id)
    student = StudentUser.objects.get(id=current_user_id)

    if(student.app_counter > 4):
        return HttpResponse('you have applied to the maximum amount of applications!')

    Course_Name = data.Course_Name
    Course_Section = data.Section
    form = courseForm1()
    if response.POST:
        form = courseForm1(response.POST, response.FILES)
        if form.is_valid() and response.FILES:

            application = form.save(commit=False)
            application.Course_Name = Course_Name
            application.Section = Course_Section
            student.app_counter+=1
            application.save()
            student.save()
            return redirect('student_landing_page')

    else:
        form = courseForm1()

    context = {
        'student' : student,
        'course' : data,
        'form' : form
    }

    return render(response, 'course_app_page.html', context)
