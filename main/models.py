from django.db import models

# Create your models here.
class SystAdmin(models.Model):
	id=models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	registration_number = models.CharField(max_length=10)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects = models.Manager()


class Programmes(models.Model):
	id=models.AutoField(primary_key=True)
	prog_name=models.CharField(max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()



class Hostels(models.Model):
	id=models.AutoField(primary_key=True)
	hostel_name=models.CharField(max_length=100)
	gender=models.CharField(max_length=20)
	price=models.DecimalField(max_digits=10, decimal_places=2)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class Rooms(models.Model):
	id=models.AutoField(primary_key=True)
	hostel_id=models.ForeignKey(Hostels, on_delete=models.CASCADE)
	room_name=models.CharField(max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class Students(models.Model):
	id=models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	registration_number=models.CharField(max_length=10)
	gender=models.CharField(max_length=10)
	prog_id=models.ForeignKey(Programmes, on_delete=models.CASCADE, default=1)
	#fees_id=models.ForeignKey(Fees, on_delete=models.CASCADE)
	level=models.CharField(max_length=100)
	room_id=models.ForeignKey(Rooms, on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()
class Accommo_Bookings(models.Model):
	id=models.AutoField(primary_key=True)
	student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
	room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
	status=models.CharField(max_length=100)
	period=models.CharField(max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class Fees(models.Model):
	id=models.AutoField(primary_key=True)
	student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
	balance=models.DecimalField(max_digits=10, decimal_places=2)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class Notifications(models.Model):
	id=models.AutoField(primary_key=True)
	student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
	message=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

