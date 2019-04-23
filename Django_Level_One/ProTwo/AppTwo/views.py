from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse('<em>My Second App</em>')

def help(request):
	dict = {'help_tag':'This is help tag'}
	return render(request, 'AppTwo/help.html', context = dict)
