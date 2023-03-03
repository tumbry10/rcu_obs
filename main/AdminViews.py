from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from main.models import *
from main.forms import AddStudentForm
from django.urls import reverse


def admin_home(request):
	return render(request, 'AdminTemplates/dashboard.html')


def add_hostel(request):
	return render(request, 'AdminTemplates/add_hostel_template.html')


def add_room(request):
	return render(request, 'AdminTemplates/add_room_template.html')

def add_room_save(request):
	if request.method != 'POST':
		return HttpResponse('Method Not Allowed')

	else:
		room_name=request.POST.get("room_name")
		gender=request.POST.get('gender')
		price=request.POST.get('price')

		try:
			room=Rooms(room_name=room_name, gender=gender, price=price)
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
	form=AddStudentForm()
	return render(request, 'AdminTemplates/add_student_template.html', {'form':form})


def add_student_save(request):
	if request.method != 'POST':
		return HttpResponse('Method Not Allowed')

	else:
		form=AddStudentForm(request.POST, request.FILES)
		if form.is_valid():
			username=form.cleaned_data['username']
			first_name=form.cleaned_data['first_name']
			last_name=form.cleaned_data['last_name']
			email=form.cleaned_data['email']
			password=form.cleaned_data['password']
			prog_id = form.cleaned_data['programmes']
			sex = form.cleaned_data['sex']
			level= form.cleaned_data['level']

			try:
				user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)
				user.students.registration_number = username
				program_obj = Programmes.objects.get(id=prog_id)
				user.students.prog_id = program_obj

				user.students.gender = sex
				user.students.level=level
				user.save()
				messages.success(request, 'Successfully Added Student')
				return HttpResponseRedirect('/add_student')

			except:
				messages.error(request, 'Failed to Add Student, Retry')
				return HttpResponseRedirect('/add_student')
		else:
			form=AddStudentForm(request.POST)
			return render(request, 'AdminTemplates/add_student_template.html', {'form':form})

def manage_room(request):
	rooms=Rooms.objects.all()
	return render(request, 'AdminTemplates/manage_room_template.html', {'rooms':rooms})

def edit_room(request, room_id):
	room=Rooms.objects.get(id=room_id)
	return render(request, 'AdminTemplates/edit_room_template.html', {'room':room, 'id':room_id})

def edit_room_save(request):
	if request.method != 'POST':
		return HttpResponse('<h2>METHOD NOT ALLOWED </h2>')
	else:
		room_id = request.POST.get('room_id')
		room_name = request.POST.get('room_name')
		gender=request.POST.get('gender')
		price=request.POST.get('price')

		try:
			room = Rooms.objects.get(id=room_id)
			room.room_name=room_name
			room.gender=gender
			room.price=price
			room.save()
			messages.success(request, 'Room Successfully Edited')
			return HttpResponseRedirect('/edit_room/'+room_id)

		except:
			messages.error(request, 'Failed to Edit Room, Retry')
			return HttpResponseRedirect('/edit_room/'+room_id)


def add_period(request):
	return render(request, 'AdminTemplates/add_period_template.html')

def add_period_save(request):
	if request.method != "POST":
		return HttpResponseRedirect(reverse('add_period'))
	else:
		start_date=request.POST.get('start_date')
		end_date=request.POST.get('end_date')

		try:
			period=SemesterPeriod(start_date=start_date, end_date=end_date)
			period.save()
			messages.success(request, 'Semester Period Successfully Added')
			return HttpResponseRedirect(reverse('add_period'))

		except:
			messages.error(request, 'Failed to Add Semester Period, Retry')
			return HttpResponseRedirect(reverse('add_period'))
