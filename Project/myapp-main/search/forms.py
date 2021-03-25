
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# import GeeksModel from models.py
from data.models import Client


# create a ModelForm
class ClientForm(forms.ModelForm):

    # specify the name of model to use 
    class Meta:
        model = Client
        fields = ['Level','Email']