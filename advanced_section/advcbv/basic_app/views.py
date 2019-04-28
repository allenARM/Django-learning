from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (View, TemplateView,
									ListView, DetailView,
									CreateView, UpdateView,
									DeleteView)
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

class SchoolCreateView(CreateView):
	fields = ('name', 'principal', 'location')
	model = models.School

class SchoolUpdateView(UpdateView):
	fields = ('name', 'principal')
	model = models.School

class SchoolDeleteView(DeleteView):
	model = models.School
	success_url = reverse_lazy("basic_app:list")
