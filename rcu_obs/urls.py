"""rcu_obs URL Configuration

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
from django.urls import path
from main import views, AdminViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage, name='ShowLoginPage'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('admin_home', AdminViews.admin_home, name='admin_home'),
    path('add_hostel', AdminViews.add_hostel, name='add_hostel'),
    path('add_hostel_save', AdminViews.add_hostel_save, name='add_hostel_save'),
    path('add_room', AdminViews.add_room, name='add_room'),
    path('add_room_save', AdminViews.add_room_save, name='add_room_save'),
    path('add_course', AdminViews.add_course, name='add_course'),
    path('add_course_save', AdminViews.add_course_save, name='add_course_save'),
    path('add_student', AdminViews.add_student, name='add_student'),
    path('add_student_save', AdminViews.add_student_save, name='add_student_save'),
]
