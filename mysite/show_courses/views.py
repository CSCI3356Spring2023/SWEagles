
#views
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import ToDoList, Item
#from .forms import CreateNewList
# Create your views here.
from course.models import AddCourseModel

# Create your views here.

def added_courses(request):
    course_list = AddCourseModel.objects.all()

    context = {
        'course_list' : course_list
    }

    return render(request, 'show_courses.html', context)
# Create your views here.
