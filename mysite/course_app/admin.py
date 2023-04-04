from django.contrib import admin
from .forms import *
from .models import *


class CustomCourseAdmin1(admin.ModelAdmin):
    form = courseForm1
    readonly_fields = ('Course_Name','Course_Section',)
    list_display = ('Course_Name', 'Course_Section', 'Discussion_Time_1', 'Discussion_Time_2', 'First_and_Last_Name', 'Resume', 'Cover_Letter', 'Reference_Letter')

class CustomCourseAdmin2(admin.ModelAdmin):
    form = courseForm2
    readonly_fields = ('Course_Name','Course_Section',)
    list_display = ('Course_Name', 'Course_Section', 'Discussion_Time_1', 'Discussion_Time_2', 'First_and_Last_Name', 'Resume', 'Cover_Letter', 'Reference_Letter')

admin.site.register(courseApplicationAllRequired, CustomCourseAdmin1)
admin.site.register(courseApplicationOnlyResume, CustomCourseAdmin2)
