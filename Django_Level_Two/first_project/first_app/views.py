from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage
# Create your views here.

def index(request):
	webpgs_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records':webpgs_list}
	return render(request, 'first_app/index.html', context = date_dict)
