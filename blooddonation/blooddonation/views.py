from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout

#Loads Home page(that contains the choices TA and Professor) if the user is authenticated and index page otherwise
def index(request):
	if request.user.is_authenticated():
		return render(request, 'blooddonation/index1.html')
	else:
		return render(request, 'blooddonation/index.html')
		
def welcome(request):
	if request.user.is_authenticated():
		return render(request, 'blooddonation/index1.html')
	else:
		return render(request, 'blooddonation/index.html')
		
def logout(request):
	"""Logs out user"""
	auth_logout(request)
	return HttpResponseRedirect('/')
