from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from main.models import *
from django.urls import reverse


def student_home(request):
	return render(request, 'StudentTemplates/student_dashboard.html')

def book_room(request):
	rooms=Rooms.objects.all()
	semesterperiod=SemesterPeriod.objects.all()
	return render(request, 'StudentTemplates/book_room_template.html', {'rooms':rooms, 'semesterperiod':semesterperiod})

def book_room_save(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse(book_room))
	else:
		room_id=request.POST.get('hostels')
		hostels=Rooms.objects.get(id=room_id)
		period_id=request.POST.get('periods')
		periods=SemesterPeriod.objects.get(id=period_id)
		status=request.POST.get('status')

		student_obj=Students.objects.get(admin=request.user.id)

		try:
			accommo_booking=Accommo_Bookings(student_id=student_obj, status=status, room_id=hostels, period_id=periods)
			accommo_booking.save()
			messages.success(request, 'Successfully Booked Accommodation')
			return HttpResponseRedirect('/book_room')

		except:
			messages.error(request, 'Failed to Book Accommodation, Retry')
			return HttpResponseRedirect('/book_room')

def my_bookings(request, student_id):
	student=Students.objects.get(admin=student_id)
	accommo_bookings=Accommo_Bookings.objects.all()
	my_bookings=student.accommo_bookings_set.all()
	return render(request, 'StudentTemplates/my_bookings_template.html', {'student':student, 'id':student_id, 'accommo_bookings':accommo_bookings, 'my_bookings':my_bookings})