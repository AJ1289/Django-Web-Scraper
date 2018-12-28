from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from bs4 import BeautifulSoup
import requests
from requests import get
# Create your views here.
def index(request):
	return render(request,'pro/login.html',{})

def sign(request):
	return render(request,'pro/signup.html',{})	

def home(request):
	return render(request,'pro/myycrousel.html',{})

def port(request):
	return render(request,'pro/portfolio.html',{})

def docu(request):
	return render(request,'pro/documentation.html',{})

def dash(request):
	return render(request,'pro/dashboard.html',{})	


@csrf_exempt
def send_data(request):
	try:
		if(request.POST):
			User.objects.create(username=request.POST['user'],first_name=request.POST['frtName'],last_name=request.POST['lrtName'],email=request.POST['mail'],password=request.POST['password'])
           
	except Exception as e:
		print('Error is ',e)
	return HttpResponse('success')	


@csrf_exempt
def log(request):
	try:
		u=request.POST['uname']

		p=request.POST['pword']
		if(u!='' or p!=''):
			z=authenticate(username=u,password=p)
			if(z=='True'):
				login(request,z)
			return HttpResponse('log_success')
		else:
			return HttpResponse('Error')
	except Exception as e:
		print('error is',e)

# ###############################################################
@csrf_exempt
def url1(request):
	f1=open('D:\\abc\\structure.txt','a')
	u=request.POST['url']
	print(u)
	url ='https://'+u
	response = get(url)
	f1.write(response.text[:])
	f1.close()
	return HttpResponse('success')


#################################################################
@csrf_exempt
def links(request):
	url =request.POST['web']
	r  = requests.get("http://" +url)
	data = r.text
	soup = BeautifulSoup(data)
	m=open('D:\\abc\\link.txt','a')
	for link in soup.find_all('a'):
		print(link.get('href'))
		m.write(link.get('href'))
		m.write("\n")
	m.close()
	return HttpResponse('link_success')

#################################################################
@csrf_exempt
def texts(request):
	url=request.POST['text']
	f2=open("D:\\abc\\text.txt",'a')
	r  = requests.get("http://" +url)
	data = r.text
	soup = BeautifulSoup(data)
	for link in soup.find_all('p'):
		f2.write(link.text)
		f2.write("\n")
		

	f2.close()
	return HttpResponse('text_success')	