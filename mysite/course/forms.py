from django import forms
from .models import AddCourseModel

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourseModel
        fields = '__all__'