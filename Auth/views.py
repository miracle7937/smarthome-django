from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail



# Create your views here.
def logoutUser(request):
    logout(request=request)
    return redirect('user-login')


def register(request):
    print(request.POST)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('email'))
            username = form.cleaned_data.get('username')
            messages.success(request, 'account created successful ' + username)
            return redirect("user-login")

    context = {
        'form': form
    }
    return render(request, 'sign_up.html', context)


def loginPage(request):
    print(request.POST)
   

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
            print('this is authenticated ' , user)
            

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request, 'email or password is not correct')
        except:
            messages.info(request, "user doesn't exist ")

    return render(request, 'sign_in.html')





# send mail


def email(request):

    send_mail('HELLO', 'THISICCCCCCCCCCCCC',
              'ebukamiracl45@mail.com', ['ebukamiracl35@mail.com'], fail_silently=False)
    return redirect('contact')







