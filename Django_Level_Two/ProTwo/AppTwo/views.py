from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
	return render(request, 'AppTwo/main.html')

def help(request):
	dict = {'help_tag':'This is help tag'}
	return render(request, 'AppTwo/help.html', context = dict)

def users(request):
	users_list = User.objects.order_by('FirstName')
	users = {'users_list': users_list}
	return render(request, 'AppTwo/users.html', context = users)
