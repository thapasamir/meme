from django.forms import ModelForm,TextInput,Textarea 
from .models import Create_Post,Create_Cateogry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Create_CateogryForm(ModelForm):
	class Meta:
		model = Create_Cateogry
		fields = ('Title','Description','photo')
		widgets = {
            'Title': TextInput(attrs={'class': 'form-control', 'id': 'validationTooltip01'}),
            'Description': Textarea(attrs={'class': 'form-control', 'id': 'validationTooltip01'}),
        }


class Create_PostForm(ModelForm):
	class Meta:
		model = Create_Post
		fields = ('Title','photo','cateogry')
		
		
class UserCreationform(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

