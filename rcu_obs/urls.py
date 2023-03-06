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
from main import views, AdminViews, StudentViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage, name='show_login'),
    path('doLogin', views.doLogin, name='do_login'),
    path('logout_user', views.logout_user, name="logout"),
    path('admin_home', AdminViews.admin_home, name='admin_home'),
    path('add_room', AdminViews.add_room, name='add_room'),
    path('add_room_save', AdminViews.add_room_save, name='add_room_save'),
    path('add_course', AdminViews.add_course, name='add_course'),
    path('add_course_save', AdminViews.add_course_save, name='add_course_save'),
    path('add_student', AdminViews.add_student, name='add_student'),
    path('add_student_save', AdminViews.add_student_save, name='add_student_save'),
    path('manage_room', AdminViews.manage_room, name='manage_room'),
    path('edit_room/<str:room_id>', AdminViews.edit_room, name='edit_room'),
    path('edit_room_save', AdminViews.edit_room_save, name='edit_room_save'),
    path('add_period', AdminViews.add_period, name="add_period"),
    path('add_period_save', AdminViews.add_period_save, name='add_period_save'),
    #path('manage_period', AdminViews.manage_period, name=manage_period),
    #path('manage_period_save', AdminViews.manage_period_save, name=manage_period_save),

    #Students urls
    path('student_home', StudentViews.student_home, name='student_home'),
    path('book_room', StudentViews.book_room, name='book_room'),
    path('book_room_save', StudentViews.book_room_save, name='book_room_save'),
    path('my_bookings<str:student_id>', StudentViews.my_bookings, name='my_bookings'),
]
