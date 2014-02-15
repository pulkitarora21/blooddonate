from django.db import models
class Register(models.Model):
	yourname=models.CharField(max_length=20)
	bloodgroup=models.CharField(max_length=4)
	phone=models.BigIntegerField(default=9999999999)
	email=models.EmailField(max_length=75, primary_key=True)
	

class Raiserequests(models.Model):
	patientname=models.CharField(max_length=20)
	bloodgroupreqd=models.CharField(max_length=4)
	phone1=models.BigIntegerField(default=9999999999)
	email1=models.EmailField(max_length=75)
	volunteername=models.CharField(max_length=20)
	volunteerbloodgroup=models.CharField(max_length=4)
	
	
class Volunteers(models.Model):
	volunteername1=models.CharField(max_length=20)
	bloodgroup1=models.CharField(max_length=4)
	phone2=models.BigIntegerField(default=9999999999)
	
	
class blood(models.Model):
	group=models.CharField(max_length=20)
	count=models.IntegerField(default=0)
	
	
	 
