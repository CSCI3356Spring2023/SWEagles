from django import forms
from django.forms import ModelForm
from .models import courseApplication

class courseForm(ModelForm):
    
    class Meta:
        model = courseApplication
        fields = ['Discussion_Time_1', 'Discussion_Time_2', 'First_and_Last_Name', 'Resume', 'Cover_Letter', 'Reference_Letter']
