from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class CustomUser(AbstractUser):
	user_type_data=((1, 'SystAdmin'), (2, 'Student'))
	user_type=models.CharField(default=1, choices=user_type_data, max_length=10)


class SystAdmin(models.Model):
	id=models.AutoField(primary_key=True)
	admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	registration_number = models.CharField(max_length=10)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects = models.Manager()

	class Meta:
		verbose_name_plural = "SystAdmins"

	def __str__(self):
		return str(self.admin)


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
	admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	registration_number=models.CharField(max_length=10)
	gender=models.CharField(max_length=10)
	prog_id=models.ForeignKey(Programmes, on_delete=models.CASCADE, default=1)
	#fees_id=models.ForeignKey(Fees, on_delete=models.CASCADE)
	level=models.CharField(max_length=100)
	room_id=models.ForeignKey(Rooms, on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

	class Meta:
		verbose_name_plural = "Students"

	def __str__(self):
		return str(self.admin)


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


#Creating signal in django so when a new user is created it will add a new rown in the sysAd and Students table with ID in admin_id column
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):  #function to add data to SystAD or Student Table
	if created:
		if instance.user_type==1:
			SystAdmin.objects.create(admin=instance)
		if instance.user_type==2:
			Students.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
	if instance.user_type==1:
		instance.systadmin.save()

	if instance.user_type==2:
		instance.students.save()