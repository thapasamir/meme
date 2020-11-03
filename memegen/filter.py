import django_filters
from .models import *
from django.forms import ModelForm,TextInput,Textarea 
from django_filters import CharFilter
class PostFilters(django_filters.FilterSet):
	Title = CharFilter(field_name='Title',lookup_expr='contains',label='search')
	class Meta:
		model = Create_Post
		fields = ['Title','cateogry']
		widgets = {
            'Title': TextInput(attrs={'class':'form-control mr-sm-2', 'type':"search", 'placeholder':'Search','aria-label':"Search"}),
            
        }
class CatFilters(django_filters.FilterSet):
	Title = CharFilter(field_name='Title',lookup_expr='contains',label='search')
	class Meta:
		model = Create_Cateogry
		fields = ['Title','Description']
		widgets = {
            'Title': TextInput(attrs={'class':'form-control mr-sm-2', 'type':"search", 'placeholder':'Search','aria-label':"Search"}),
            
        }