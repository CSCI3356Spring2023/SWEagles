from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import ToDoList, Item
#from .forms import CreateNewList
# Create your views here.
from course_app.models import courseApplicationAllRequired, courseApplicationOnlyResume
from register.models import StudentUser

# Create your views here.

def view_applications(request):
    current_user = request.user.username
    # get applications with file 
    application_list_1 =  courseApplicationAllRequired.objects.all()
    application_list_1 = application_list_1.filter(Username=current_user)
    
    # get file optional applications
    application_list_2 =  courseApplicationOnlyResume.objects.all()
    application_list_2 = application_list_2.filter(Username=current_user)
    
    # append sets
    combined_applications = chain(application_list_1, application_list_2)
    
    return render(request, 'student_view_applications.html', {'custom_attribute': combined_applications})