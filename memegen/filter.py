import django_filters
from .models import *
from django_filters import CharFilter
class PostFilters(django_filters.FilterSet):
	Title = CharFilter(field_name='Title',lookup_expr='contains')
	class Meta:
		model = Create_Post
		fields = ['Title','cateogry']
		
