from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import NewUser
# Create your views here.

def index(request):
	return render(request, 'AppTwo/main.html')

def help(request):
	dict = {'help_tag':'This is help tag'}
	return render(request, 'AppTwo/help.html', context = dict)

def users(request):
	form = NewUser()

	if request.method == 'POST':
		form = NewUser(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("ERROR")
	return render(request, 'AppTwo/users.html', {'form':form})
