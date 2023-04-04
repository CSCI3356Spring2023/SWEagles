from django.shortcuts import render, redirect
from .forms import AddCourseForm
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
        return redirect('instructor_landing_page')

    context = {
        'form' : form
    }

    return render(request, 'course_creation.html', {'form': form})
