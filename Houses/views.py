
# Create your views here.
from django.shortcuts import render, redirect
from .models import Properties,  Subscription, SubBreakDown, Tour
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from .filters import Titlefilter
from django.contrib import messages



# Create your views here.

@login_required(login_url='user-login')
def home(request):
    house = Properties.objects.all()
    count = Subscription.objects.filter(user=request.user)

    print(count)
    context = {
        'house': house,
        'mysub': count
    }

    return render(request, 'main.html', context)



@login_required(login_url='user-login')
def detailPage(request, id):
    house = Properties.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        email = request.POST.get('email')
        number = request.POST.get('number')

        date = request.POST.get('date')
        tour = Tour.objects.create(dateOfTour=date, name=name, email=email, phoneNumber=number )
        
        tour.save()
        messages.success(request, 'A tour have been scheduled')

        
        print(request.POST)
    print(house, 'my house')
    context = {
        'house': house
    }
    return render(request, 'propertyDetail.html', context)


@login_required(login_url='user-login')
def subform(request, id):
    print(request.POST)
    house = Properties.objects.get(id=id)
    
    
    if request.method == 'POST':
        
        fullName = request.POST.get('fullName')
        address = request.POST.get('address')
        phoneNumber = request.POST.get('phoneNumber')
        city = request.POST.get('city')
        state = request.POST.get('state')
        kin_Name = request.POST.get('kin_Name')
        kin_phoneNumber = request.POST.get('kin_phoneNumber')
        kin_address = request.POST.get('kin_address')

        employer_name = request.POST.get('employer_name')
        employer_Address = request.POST.get('employer_Address')
        selected_house =  house
        amount = house.price
        amount_to_be_paid= amount/10
        total_payed = 0

        subscription = Subscription.objects.create( user=request.user,  fullName=fullName,
        address=address, phoneNumber=phoneNumber,city=city,
        state=state, kin_Name= kin_Name, kin_phoneNumber= kin_phoneNumber,
                                                    kin_address=kin_address, employer_name=employer_name, employer_Address=employer_Address, house=selected_house,
                                                    amount=amount, amount_to_be_paid=amount_to_be_paid, total_paid=total_payed

        )
     
        subscription.save()
       

        



        return redirect('sublist')
       
    
    return render(request, 'subscribe_form.html')


@login_required(login_url='user-login')

def listOfSub(request):
    if request.user.is_authenticated:

        sub_list = Subscription.objects.filter(user=request.user)
        
        print(sub_list)
        if len(sub_list) ==0:
            return render(request, 'empty-sub.html',)
        context = {
            'subs': sub_list
        }
        return render(request, 'subscription_List.html', context)
    
    else:
        raise Http404()


@login_required(login_url='user-login')
def tableList(request, id):
    sub = Subscription.objects.get(user=request.user, pk=id)

    table = SubBreakDown.objects.filter(subscriber= sub)
    count = Subscription.objects.filter(user=request.user)
    print(table)
    



    context ={
        'breakdowns': table,
        'property': sub.house.title,
        'mysub': count
    }
    return render(request, 'sub_table.html', context)


@login_required(login_url='user-login')
def properties(request):

     house = Properties.objects.all()
     count = Subscription.objects.filter(user=request.user)
    
     property_filter = Titlefilter(request.GET, queryset=house)
     house= property_filter.qs
     print(house)

     print(count)
     context = {
        'house': house,
        'mysub': count,
        'number': house.count(),
        'filter': property_filter
     }


     return render(request, 'properties.html', context)


@login_required(login_url='user-login')
def contact(request):
    count = Subscription.objects.filter(user=request.user)

    print(count)
    context = {
        
        'mysub': count,
        
    }
    return render(request, 'contact.html',context)




