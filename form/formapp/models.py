from django.db import models

# Create your models here.


class Contact(models.Model):
    f_name = models.CharField(max_length=999,primary_key=True,default='First Name')
    l_name = models.CharField(max_length=999,default='Last Name')
    phone_number = models.CharField(max_length=999,default='Phone Number')
    email = models.CharField(max_length=999,default='Enter your email')
    address = models.CharField(max_length=999,default='Enter Local Address')
    password = models.CharField(max_length=999,default="YOUR PASSWORD")


    def __str__(self):
        return self.f_name