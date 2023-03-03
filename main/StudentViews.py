from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from main.models import *


def student_home(request):
	return render(request, 'StudentTemplates/student_dashboard.html')

def book_room(request):
	hostels=Hostels.objects.all()
	rooms=Rooms.objects.all()
	return render(request, 'StudentTemplates/book_room_template.html', {'hostels':hostels, 'rooms':rooms})

def book_room_save(request):
	pass 