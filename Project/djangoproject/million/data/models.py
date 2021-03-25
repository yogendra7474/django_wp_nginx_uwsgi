from django.db import models
class Client(models.Model):
	First_Name = models.CharField(max_length=250, blank=True)
	Last_Name = models.CharField(max_length=250, blank=True)
	Company = models.CharField(max_length=250, blank=True)
	Website = models.CharField(max_length=250, blank=True)
	Title = models.CharField(max_length=250, blank=True)
	Email = models.CharField(max_length=250, blank=True)
	Email_Confidence = models.CharField(max_length=250, blank=True)
	Address = models.CharField(max_length=250, blank=True)
	Primary_Department = models.CharField(max_length=250, blank=True)
	Secondary_Department = models.CharField(max_length=250, blank=True)
	Level = models.CharField(max_length=250, blank=True)
	Street = models.CharField(max_length=250, blank=True)
	City = models.CharField(max_length=250, blank=True)
	State = models.CharField(max_length=250, blank=True)
	Zip = models.CharField(max_length=250, blank=True)
	Country = models.CharField(max_length=250, blank=True)
	LinkedIn = models.CharField(max_length=250, blank=True)
	Twitter = models.CharField(max_length=250, blank=True)
	Facebook = models.CharField(max_length=250, blank=True)
	Industry = models.CharField(max_length=250, blank=True)
	Company_Headcount = models.CharField(max_length=250, blank=True)
	Company_Revenue = models.CharField(max_length=250, blank=True)
	Direct_Dial = models.CharField(max_length=250, blank=True)
	Mobile_Number = models.CharField(max_length=250, blank=True)
	Company_Number = models.CharField(max_length=250, blank=True)
	Other_Number = models.CharField(max_length=250, blank=True)
	Email_Encrypt = models.CharField(max_length=250, blank=True)
	Mobile_Number_Encrypt = models.CharField(max_length=250, blank=True)


	def __str__(self):
		return self.First_Name

