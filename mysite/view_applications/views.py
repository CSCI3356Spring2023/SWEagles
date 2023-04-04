from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import ToDoList, Item
#from .forms import CreateNewList
# Create your views here.
from course_app.models import courseApplicationAllRequired, courseApplicationOnlyResume

# Create your views here.

def view_applications(request, custom_attribute):
    current_user = request.user
    # get applications with file 
    application_list_1 =  courseApplicationAllRequired.objects.all()
    application_list_1 = application_list_1.filter(Course_Name=custom_attribute)
    
    # get file optional applications
    application_list_2 =  courseApplicationOnlyResume.objects.all()
    application_list_2 = application_list_2.filter(Course_Name=custom_attribute)
    
    # append sets
    combined_applications = chain(application_list_1, application_list_2)
    
    return render(request, 'view_applications.html', {'custom_attribute': combined_applications})


