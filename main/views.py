from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'index.html')

def ShowLoginPage(request):
	return render(request, 'login_page.html')

def doLogin(request):
	return render(request, 'AdminTemplates/dashboard.html')


