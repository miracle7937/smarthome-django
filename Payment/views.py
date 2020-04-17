from django.shortcuts import render, redirect
from .forms import CustomerInfoForm
from django.http.response import HttpResponse
from Houses.models import SubBreakDown, Subscription
import datetime
# Create your views here.



def success_pay(request, pk):
    date =datetime.datetime.now()
    sub = Subscription.objects.get(id=pk, user=request.user)
    total = sub.amount
    amount_paid = sub.amount_to_be_paid
   
    # updating the total amount
    total_paid = sub.total_paid
    updatedAmount = total_paid+amount_paid
    sub.total_paid = updatedAmount
    sub.save()
    percentage = 100*(updatedAmount)/(total)
    
    SubBreakDown.objects.create(user= request.user ,  subscriber=sub, date=date,
                                payment_month=True, total=total, amount_paid=amount_paid, percentage=percentage, updatedAmount=updatedAmount)
    print(sub)
    return redirect('success_message')


def message(request):


    return render(request, 'Payment/paystack.html')
