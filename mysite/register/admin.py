from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role')

class StudentUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'app_counter')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(StudentUser, StudentUserAdmin)
