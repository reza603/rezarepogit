
from django.contrib import admin
from django.urls import path,include
from django.views import generic
from . import views


urlpatterns = [
   
    # path('show/', include('timetable.urls')),
     path('show/', views.show,name='show'),

]

