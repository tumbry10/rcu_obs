from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
#from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.
def home(request):
	return render(request, 'index.html')

def ShowLoginPage(request):
	return render(request, 'login_page.html')

def doLogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)
		#if user is not None
		if user != None:
			login(request, user)
			if user.user_type=="1":
				return HttpResponseRedirect(reverse('admin_home'))
			else:
				return HttpResponseRedirect(reverse("student_home"))
		else:
			messages.error(request, 'INVALID LOGIN DETAILS')
			return HttpResponseRedirect("/")

def logout_user(request):
	logout(request)
	return HttpResponseRedirect ("/")