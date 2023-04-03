from django.contrib import admin
from .forms import courseForm
from .models import courseApplication


class CustomCourseAdmin(admin.ModelAdmin):
    form = courseForm
    readonly_fields = ('Course_Name','Course_Section',)
    list_display = ('Course_Name', 'Course_Section', 'Discussion_Time_1', 'Discussion_Time_2', 'First_and_Last_Name', 'Resume', 'Cover_Letter', 'Reference_Letter')

admin.site.register(courseApplication, CustomCourseAdmin)
