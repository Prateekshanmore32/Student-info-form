from django.contrib import admin
from django.urls import path
from studentapp import views
urlpatterns = [
    path('', views.home,name='studentapp'),
    path('studentData', views.student_data,name='studentData')
]
