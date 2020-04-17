


from django.urls import path, include

from .import views

urlpatterns = [

    path('register/', views.register, name='user_register'),
    path('login/', views.loginPage, name='user-login'),
    path('logout/', views.logoutUser, name='logout'),
    path('sendmail/', views.email, name='sendmail'),

   
   

   

]
