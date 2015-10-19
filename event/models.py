from django.db import models

# Create your models here.

class Picture(models.Model):
	title_text=models.CharField(max_length=200)
	picture_url=models.CharField(max_length=600)
	description=models.TextField()
	def __str__(self):
		return self.title_text
