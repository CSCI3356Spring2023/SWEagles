from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import ToDoList, Item
#from .forms import CreateNewList
# Create your views here.
from course_app.models import  courseApplication

# Create your views here.

def view_applications(request, custom_attribute):
    current_user = request.user
    application_list =  courseApplication.objects.all()
    application_list = application_list.filter(Course_Name=custom_attribute)
    
    return render(request, 'view_applications.html', {'custom_attribute': application_list})


