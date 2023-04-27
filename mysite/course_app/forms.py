from django import forms
from django.forms import ModelForm
from .models import *

class courseForm1(ModelForm):

    class Meta:
        model = courseApplicationAllRequired
        fields = ['Discussion_Time_1', 'Discussion_Time_2', 'First_and_Last_Name', 'Username', 'Resume', 'Cover_Letter', 'Reference_Letter', 'Anything_you_want_to_add']

class courseForm2(ModelForm):

    class Meta:
        model = courseApplicationOnlyResume
        fields = ['Discussion_Time_1', 'Discussion_Time_2', 'First_and_Last_Name', 'Username','Resume', 'Cover_Letter', 'Reference_Letter', 'Anything_you_want_to_add']
