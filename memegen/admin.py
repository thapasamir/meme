from django.contrib import admin
from .models import Create_Post,Create_Cateogry



@admin.register(Create_Post)
class Create_PostAdmin(admin.ModelAdmin):
	  fields = ('Title','photo','cateogry')

@admin.register(Create_Cateogry)
class Create_CateogryAdmin(admin.ModelAdmin):
	fields = ('Title','photo','Description')

