from django.shortcuts import render, redirect
from .forms import AddCourseForm
from course.models import AddCourseModel
from register.models import CustomUser
from mysite.utils import send_email
# Create your views here.

def send_course_creation_email(response, course_id, current_user_id):


    data = AddCourseModel.objects.get(id=course_id)
    instructor = CustomUser.objects.get(id=current_user_id)

    Course_Name = data.Course_Name

    # Send successful application email
    message = "Hi "+instructor.get_full_name()+",\n\n Thank you for creating the " + Course_Name+ " course!"
    message += " You will be notified when any applications are sent in, and when any TA accepts or rejects the position." 
    message += "\n\nBest,\n The SWEagles Team"
    subject = "Thank you for creating the " + Course_Name + " course"

    send_email(instructor.email, subject, message)   

def add_course_view(request):

    Instructor_Name = request.user.username
    Instructor_ID = request.user.id
    form = AddCourseForm(request.POST or None)
    if form.is_valid():
        application = form.save(commit=False)
        application.Instructor_Name = Instructor_Name
        application.Instructor_ID = Instructor_ID
        application.save()
        form = AddCourseForm()
        return redirect('view_courses_instructor')

    context = {
        'form' : form
    }

    return render(request, 'course_creation.html', {'form': form})

def edit_course_view(response, course_id):
    Instructor_Name = response.user.username
    Instructor_ID = response.user.id
    data = AddCourseModel.objects.get(Course_ID=course_id)
    form = AddCourseForm()
    if response.POST:
        form = AddCourseForm(response.POST, instance=data)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.Instructor_Name = Instructor_Name
            edit.Instructor_ID = Instructor_ID
            edit.save()
            return redirect('view_courses_instructor')

    else:
        form = AddCourseForm(instance=data)

    context = {
        'course' : data,
        'form' : form
    }

    return render(response, 'edit_course.html', context)
    
