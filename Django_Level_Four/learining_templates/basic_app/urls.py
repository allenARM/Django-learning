from basic_app import views
from django.urls import path

#template tagging

app_name = 'basic_app'

urlpatterns = [
	path('relative/', views.relative, name = 'relative'),
	path('other/', views.other, name = 'other'),
]
