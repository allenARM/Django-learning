from django.shortcuts import render
from basicapp import forms
# Create your views here.

def index (request):
	return render(request, 'basicapp/index.html')

def form_name_view(request):
	form = forms.FormsName()

	if (request.method == 'POST'):
		form = forms.FormsName(request.POST)

		if form.is_valid():
			print("validation success")
			print("name " + form.cleaned_data['name'])
			print("EMAIL " + form.cleaned_data['email'])
			print("Text " + form.cleaned_data['text'])

	return render(request, 'basicapp/form.html', {'form':form})
