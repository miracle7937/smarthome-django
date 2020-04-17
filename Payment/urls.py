from django.urls import path, include

from .import views


urlpatterns = [

    path('sub-list/paystack/success/<int:pk>/',
         views.success_pay, name='success'),
    path('mesage/',
         views.message, name='success_message'),

]

