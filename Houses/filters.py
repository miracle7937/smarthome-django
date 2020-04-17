
import django_filters
from .models import Properties
from django_filters import  CharFilter
from django import forms





class  Titlefilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', widget=forms.TextInput(
        attrs={'class': "form-control mr-sm-2", 'placeholder': "search properties "}),)

    class Meta:
        model = Properties
        fields = ['title']
