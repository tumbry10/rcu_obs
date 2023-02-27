from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from main.models import *


def admin_home(request):
	return render(request, 'AdminTemplates/dashboard.html')


def add_hostel(request):
	return render(request, 'AdminTemplates/add_hostel_template.html')

def add_hostel_save(request):
	if request.method != 'POST':
		return HttpResponse('Not Allowed')

	else:
		hostel_name=request.POST.get('hostel_name')
		gender=request.POST.get('gender')
		price=request.POST.get('price')

		try:
			hostel_model = Hostels(hostel_name=hostel_name, gender=gender, price=price)
			hostel_model.save()
			messages.success(request, 'Hostel Successfully Added')
			return HttpResponseRedirect('/add_hostel')
		except:
			messages.error(request, 'Failed to Add Hostel, Retry')
			return HttpResponseRedirect('/add_hostel')

def add_room(request):
	hostels=Hostels.objects.all()   #For Hostels to show in the add room page
	return render(request, 'AdminTemplates/add_room_template.html', {'hostels':hostels})

def add_room_save(request):
	if request.method != 'POST':
		return HttpResponse('Method Not Allowed')

	else:
		room_name=request.POST.get("room_name")
		hostel_id=request.POST.get("hostels")
		hostels=Hostels.objects.get(id=hostel_id)

		try:
			room=Rooms(room_name=room_name, hostel_id=hostels)
			room.save()
			messages.success(request, 'Room Successfully Added')
			return HttpResponseRedirect('/add_room')
		except:
			messages.error(request, 'Failed to Add Room, Retry')
			return HttpResponseRedirect('/add_room')

def add_course(request):
	return render(request, 'AdminTemplates/add_course_template.html')

def add_course_save(request):
	if request.method != 'POST':
		return HttpResponse('Not Allowed')

	else:
		prog_name=request.POST.get('prog_name')

		try:
			prog_model = Programmes(prog_name=prog_name)
			prog_model.save()
			messages.success(request, 'Program Successfully Added')
			return HttpResponseRedirect('/add_course')
		except:
			messages.error(request, 'Failed to Add Program, Retry')
			return HttpResponseRedirect('/add_course')

def add_student(request):
	programmes=Programmes.objects.all()    #for programs to show on the add students page
	return render(request, 'AdminTemplates/add_student_template.html', {"programmes":programmes})


def add_student_save(request):
	if request.method != 'POST':
		return HttpResponse('Method Not Allowed')

	else:
		username=request.POST.get('username')
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		prog_id = request.POST.get('programmes')
		sex = request.POST.get('sex')
		level= request.POST.get('level')

		#try:
		user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)
		user.students.registration_number = username
		program_obj = Programmes.objects.get(id=prog_id)
		user.students.prog_id = program_obj

		user.students.gender = sex
		user.students.level=level
		user.save()
		messages.success(request, 'Successfully Added Student')
		return HttpResponseRedirect('/add_student')