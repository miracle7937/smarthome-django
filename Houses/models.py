from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal


# Create your models here.
LABEL_CHOICES = (
    ('For Sale', 'For Sale'),
    ('For Rent', 'For Rent'),

)


class Properties(models.Model):

    label = models.CharField(
        max_length=20, choices=LABEL_CHOICES, default='For_Sale')

    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True,  blank=True)
    image3 = models.ImageField(null=True,  blank=True)
    image4 = models.ImageField(null=True, blank=True)
    des = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100)
    price = models.IntegerField()

    size = models.IntegerField(null=True)
    bedroom = models.IntegerField(null=True)
    bathroom = models.CharField(max_length=100)












class  Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(Properties, on_delete=models.CASCADE , null= True)


    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)

    kin_Name = models.CharField(max_length=100, null=True)
    kin_phoneNumber = models.CharField(max_length=100, null=True)
    kin_address = models.CharField(max_length=100, null=True)

    employer_name = models.CharField(max_length=100, null=True)
    employer_Address = models.CharField(max_length=100, null=True)
    date = models.DateTimeField( default= datetime.now() )
    amount = models.IntegerField(null=True)
    amount_to_be_paid = models.IntegerField(null=True)
    total_paid = models.IntegerField(null=True)




class SubBreakDown(models.Model):
    subscriber = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    payment_month = models.BooleanField(default=False)
    amount_paid = models.CharField(max_length=100, blank=True)
    total = models.DecimalField(max_digits=40, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now())
    percentage = models.CharField(max_length=100, blank=True)
    updatedAmount = models.IntegerField(null=True)




class Tour(models.Model):
    dateOfTour= models.DateTimeField(default=datetime.now())
    name =  models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
