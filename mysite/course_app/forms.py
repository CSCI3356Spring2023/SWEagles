from django import forms
from course.models import AddCourse

class courseApplication(UserCreationForm):
    course = forms.ChoiceField(choices=AddCourse.objects.filter("Course_Name"))
    
