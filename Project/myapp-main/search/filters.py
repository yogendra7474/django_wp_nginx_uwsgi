import django_filters
from django.db.models import Q, Value as V, CharField
from django.db.models.functions import Concat
from multiselectfield import MultiSelectField
from django.forms.widgets import TextInput

from . import forms
from data.models import Client

class ClientFilter(django_filters.FilterSet):
    Company = django_filters.CharFilter(field_name="Company", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Company Name'}))

    Title = django_filters.CharFilter(field_name="Title", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Title'}))

    Dept = django_filters.CharFilter(field_name="Secondary_Department", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Department'}))

    Level = django_filters.CharFilter(field_name="Level", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Seniority Level'}))

    Name = django_filters.CharFilter(method='my_custom_filter', label=False, widget=TextInput(attrs={'placeholder': 'Contact Name'}))
    
    Industry = django_filters.CharFilter(field_name="Industry", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Industry'}))

    Secondary_Department = django_filters.CharFilter(field_name="Secondary_Department", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Function'}))

    Country = django_filters.CharFilter(field_name="Country", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Geography'}))
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Client.objects.all(),
    #                                                   widget=forms.CheckboxSelectMultiple)
    class Meta:

        model = Client
        fields = ['Company', 'Level', 'Dept']

    # def my_custom_filter(self, queryset, name, value):
    #     return Client.objects.annotate(Name=Concat('First_Name', V(' ('), 'Last_Name', V(')')
    #                                                ,output_field=CharField())).filter(Name__icontains=value)