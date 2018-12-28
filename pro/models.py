from django.db import models

class Request(models.Model):
	# uid=models.Foreignkey('auth.User')
	username=models.CharField(max_length=200)
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	rpassword=models.CharField(max_length=200)