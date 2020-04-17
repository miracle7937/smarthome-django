from django.db import models
# Create your models here.


class CustomerInfo(models.Model):

    
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    full_name = models.CharField(max_length=150)
