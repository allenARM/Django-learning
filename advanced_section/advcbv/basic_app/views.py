from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

class IndexView(TemplateView):
	template_name = 'index.html'

class SchoolListView(ListView):
	#context_object_name changes default name of return variable
	context_object_name = 'schools'
	model = models.School
	#by default ListView creates return variable by using class name and appeding "_list"

class SchoolDetailView(DetailView):
	context_object_name = 'school_detail'
	model = models.School
	template_name = 'basic_app/schooldetail.html'
