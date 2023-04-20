from django.shortcuts import render, redirect
from .forms import AddCourseForm
from course.models import AddCourseModel
# Create your views here.

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
    
