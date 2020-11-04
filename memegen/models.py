from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

class Create_Cateogry(models.Model):
	Title = models.CharField(max_length=100,null=True)
	Description = models.CharField(max_length=100,null=True)
	photo = CloudinaryField('image')
	upload_date = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return self.Title


class Create_Post(models.Model):
	Title = models.CharField(max_length=100,null=True)
	photo = CloudinaryField('image')
	upload_date = models.DateTimeField(auto_now_add=True, blank=True,)
	cateogry = models.ManyToManyField(Create_Cateogry)

	def __str__(self):
		return self.Title

