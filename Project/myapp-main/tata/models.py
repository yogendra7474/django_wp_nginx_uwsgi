from django.db import models
class tiktok(models.Model):
	First_Name = models.CharField(max_length=250)

	def __str__(self):
		return self.First_Name

