import requests 
from django.shortcuts import render,reverse,redirect
from asyncio.windows_events import NULL
from email.errors import NonASCIILocalPartDefect
import json

from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.shortcuts import render,HttpResponseRedirect,Http404

from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import Services
from cart.forms import AddToCartProductForm

def get_context_data(self,**kwargs):
    context=super.get_context_data(**kwargs)
    context['add_to_cart_form']=AddToCartProductForm()
    return context
def cardetails(request):
    #   response=None
    #   url= "https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    #   payload = "{\n\t\"registrationNumber\": \"AA19AAA\"\n}"
    #   headers = {
    #             'Content-Type': 'application/json',
    #               'x-api-key': 'yqBj6UpOLH59bhVWyoAgLMDEhwwlic7uS8FQ8b80'
                   
    #            }

    #   my_dict = requests.request("POST", url, headers=headers, data = payload)
    #   info=my_dict.json() # 👉️ <class 'str'>
     
       
       
    #   print(info["engineCapacity"])
      return render( request,'services/cardetails.html')
def showServicePerApi(request):

         
           return render( request,'services/servicesStep2.html')
        #    return (response.text.encode('utf8'))
                  
class getallservicesviewstep2(generic.ListView):
    model=Services
    template_name = 'services/servicesStep2.html'
    context_object_name ='services'

class getallservicesview(generic.ListView):
    model=Services
    template_name = 'services/services.html'
    context_object_name ='services'


    def get_queryset(self):
        return Services.objects.filter(status='pub').order_by('-date_modified')


class ServiceDetailView(generic.DetailView):

    model=Services
    template_name = 'services/service_detail.html'
    context_object_name = 'services'



class ServiceCreateView(generic.CreateView):

     model = Services
     fields = ['title','text','price','author','status']
     template_name = 'services/services_create.html'







