from django.urls import path, include

from .import views  


urlpatterns = [


    path('', views.home, name='home'),
    path('detail/<id>/', views.detailPage, name='detail_page'),
    path('detail/<id>/subscribe/', views.subform, name='subform'),
    path('sub-list/', views.listOfSub, name='sublist'),
    path('table/<id>/', views.tableList, name='tableList'),
    path('properties/', views.properties, name='properties'),

    path('contact/', views.contact, name='contact'),





]
