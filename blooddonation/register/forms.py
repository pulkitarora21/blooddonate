from django import forms

from django.forms.widgets import *
from register.models import *

class c_form(forms.ModelForm):
	yourname= forms.CharField(required=True,widget=forms.TextInput) #course number
	bloodgroup= forms.CharField(required=True,widget=forms.TextInput) #course name
	phone= forms.IntegerField(required=True,widget=forms.TextInput) #strength of students
	email= forms.CharField(required=True,widget=forms.TextInput) #strength of TA's
	class Meta:
		model = Register
		fields = ('yourname','bloodgroup','email')
		
class req_form(forms.ModelForm):
	patientname= forms.CharField(required=True,widget=forms.TextInput) 
	bloodgroupreqd = forms.CharField(required=True,widget=forms.TextInput) 
	phone1 = forms.IntegerField(required=True,widget=forms.TextInput) 
	email1 = forms.CharField(required=True,widget=forms.TextInput) 
	volunteername = forms.CharField(required=True,widget=forms.TextInput) 
	volunteerbloodgroup = forms.CharField(required=True,widget=forms.TextInput) 
	
	class Meta:
		model = Raiserequests
		fields = ('patientname','bloodgroupreqd','phone1','email1', 'volunteername', 'volunteerbloodgroup')

class vol_form(forms.ModelForm):
	volunteername1 = forms.CharField(required=True,widget=forms.TextInput) 
	bloodgroup1 = forms.CharField(required=True,widget=forms.TextInput) 
	phone2 = forms.IntegerField(required=True,widget=forms.TextInput) 
	
	
	class Meta:
		model = Volunteers
		fields = ( 'volunteername1','bloodgroup1', 'phone2')
