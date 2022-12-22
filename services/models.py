from django.db import models
from django.shortcuts import reverse


class Services (models.Model):




     STATUSE_CHOISES=(
       ('pub','done'),
       ('drf','register'),
      )
     id=models.BigAutoField
     title= models.CharField(max_length=100)
     text= models.CharField(max_length=100)
     author= models.ForeignKey('auth.user',on_delete=models.CASCADE,blank=True)
     date_created =models.DateTimeField(auto_now_add=True)
     date_modified = models.DateTimeField(auto_now=True)
     status= models.CharField(choices=STATUSE_CHOISES,max_length=3)
     price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
     price2 = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
     price3 = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
     pic=models.CharField(max_length=100)



     def __str__(self):
         return   str(self.price)




     def __str__(self):
         return self.id



     def get_absolute_url(self):
        return reverse('service_detail',args=[self.id])




