from home.models import ContactInformation
from home.models import ProfileData
from django import forms


class ContactForm(forms.Form):
    First_Name = forms.CharField(label='First_Name', max_length=100)
    Last_Name = forms.CharField(label='Last_Name', max_length=100)
    Email = forms.EmailField(label='Email', max_length=100)
    Phone_Number = forms.CharField(label='Phone_Number', max_length=100)
    # class Meta:
    #     model = ContactInformation
    #     fields = ['First_Name', 'Last_Name', 'Email', 'Phone_Number']


class ProfileDataForm(forms.Form):
    SaveTitle = forms.CharField(label='SaveTitle', max_length=100)
    SaveField = forms.CharField(label='SaveField', max_length=5000)

