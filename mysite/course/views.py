from django.shortcuts import render
# Create your views here.

def course_creation(request):
    if request.method == 'POST':
        # logic for saving course creation form data to database
        pass
    else:
        # render the course creation form template
        return render(request, 'course_creation.html')