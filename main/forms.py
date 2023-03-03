from django import forms
from main.models import *


class AddStudentForm(forms.Form):
	username=forms.CharField(label='Registration Number', max_length=10, widget=forms.TextInput(attrs={"class":"form-control"}))
	first_name=forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
	last_name=forms.CharField(label='Surname', max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
	email=forms.EmailField(label='Email Address', max_length=100, widget=forms.EmailInput(attrs={"class":"form-control"}))
	password=forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control"}))
	program_list=[]
	try:
		programmes=Programmes.objects.all()
		
		for program in programmes:
			small_program = (program.id, program.prog_name)
			program_list.append(small_program)
	except:
		program_list=[]

	gender_choices=(
		('Male', 'Male'),
		('Female', 'Female'),
	)

	programmes=forms.ChoiceField(label='Program', choices=program_list, widget=forms.Select(attrs={'class':'form-control'}))
	level=forms.CharField(label='level', max_length=10, widget=forms.TextInput(attrs={"class":"form-control"}))
	sex=forms.ChoiceField(label='Gender', choices=gender_choices, widget=forms.Select(attrs={'class':'form-control'}))

class EditStudentForm(forms.Form):
	username=forms.CharField(label='Registration Number', max_length=10, widget=forms.TextInput(attrs={"class":"form-control"}))
	first_name=forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
	last_name=forms.CharField(label='Surname', max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
	email=forms.EmailField(label='Email Address', max_length=100, widget=forms.EmailInput(attrs={"class":"form-control"}))
	programmes=Programmes.objects.all()
	program_list=[]
	try:
		programmes=Programmes.objects.all()
		
		for program in programmes:
			small_program = (program.id, program.prog_name)
			program_list.append(small_program)
	except:
		program_list=[]
	gender_choices=(
		('Male', 'Male'),
		('Female', 'Female'),
	)

	programmes=forms.ChoiceField(label='Program', choices=program_list, widget=forms.Select(attrs={'class':'form-control'}))
	level=forms.CharField(label='level', max_length=10, widget=forms.TextInput(attrs={"class":"form-control"}))
	sex=forms.ChoiceField(label='Gender', choices=gender_choices, widget=forms.Select(attrs={'class':'form-control'}))