"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as register_view
from login import views as login_view
from landing_page import views as landing_view
from course import views as course_views
from home_page import views as home_views
from course_app import views as course_app_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("register/", register_view.register, name="register"),
    path("login/", login_view.login_view, name="register"),
    path('logout/', login_view.logout_view, name='logout'),
    path('landing/', landing_view.landing_page, name='landing'),
    path('course_creation/', course_views.course_creation, name='course_creation'),
    path('home/', home_views.home_view, name='home'),
    path('course_app/', course_app_views.course_app_page, name='course_app')

]