from django.db import models

class Create_Cateogry(models.Model):
	Title = models.CharField(max_length=100,null=True)
	Description = models.CharField(max_length=100,null=True)
	photo = models.ImageField(blank=False,null=True,upload_to='cateogry/')
	upload_date = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return self.Title


class Create_Post(models.Model):
	Title = models.CharField(max_length=100,null=True)
	photo = models.ImageField(blank=False,null=True,upload_to='post/')
	upload_date = models.DateTimeField(auto_now_add=True, blank=True,)
	cateogry = models.ManyToManyField(Create_Cateogry)

	def __str__(self):
		return self.Title

