from django.db import models
from accounts.models import User

class ContactInformation(models.Model):
    First_Name = models.CharField(max_length=150)
    Last_Name = models.CharField(max_length=150)
    Email = models.EmailField(max_length=150)
    Phone_Number = models.CharField(max_length=150)
    
    def __str__(self):
        return self.First_Name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=150,blank=True)
    Last_Name = models.CharField(max_length=150,blank=True)
    DateOfBirth= models.DateField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.user.email} Profile'


class DownloadFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(blank=False, null=False)
    DownloadItems = models.TextField(max_length=5000, default=False)

    def __str__(self):
        return self.DownloadItems

class UserCredit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Credit = models.IntegerField(blank=True, null=True)
    DefaultCredit=models.IntegerField(blank=True, null=True,default=int(100))
    TotalDownload = models.IntegerField(blank=True, null=True)
    DownloadedContacts = models.TextField(max_length=5000, default=False)


    def __str__(self):
        return f'{self.user.email} UserCredit'


class ProfileData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SaveTitle = models.CharField(max_length=150)
    SaveField = models.TextField(max_length=5000, default=False)
    

    def __str__(self):
        return self.SaveField

class SavedUserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SavedId = models.TextField(max_length=5000, default=False)
    

    def __str__(self):
        return self.SavedId

