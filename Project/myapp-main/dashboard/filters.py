import django_filters
from django.db.models import Q, Value as V, CharField
from django.db.models.functions import Concat
from multiselectfield import MultiSelectField
from data.models import Client
from django.forms.widgets import TextInput

class ClientFilter(django_filters.FilterSet):
    LevelChoice = [
        ("VP-Level", "VP-Level"), 
        ("Director-Level", "Director-Level"), 
        ("Manager-Level", "Manager-Level"), 
        ("Staff", "Staff"), 
        ("Other", "Other"), 
        ("Other", "Other"),
        ]
    Company = django_filters.CharFilter(field_name="Company", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Company Name'}))

    Title = django_filters.CharFilter(field_name="Title", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Title'}))

    Dept = django_filters.CharFilter(field_name="Secondary_Department", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Department'}))

    # Name = django_filters.CharFilter(method='my_custom_filter', label=False, widget=TextInput(attrs={'placeholder': 'Contact Name'}))
    
    Industry = django_filters.CharFilter(field_name="Industry", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Industry'}))

    Secondary_Department = django_filters.CharFilter(field_name="Secondary_Department", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Function'}))

    Country = django_filters.CharFilter(field_name="Country", lookup_expr='icontains', label=False, widget=TextInput(attrs={'placeholder': 'Geography'}))
    # Level = django_filters.ChoiceFilter(field_name="Level", label=False, choices=LevelChoice)
    # # Department = django_filters.CharFilter(method='my_custom_dep', label='Department')
    # Name = django_filters.CharFilter(max_length=255, lookup_expr='icontains', label='Name')
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Client.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:

        model = Client
        fields = ['First_Name', 'Company', 'Title', 'Dept', 'Level', 'Industry', 'Secondary_Department', 'Country']

    # full_name = django_filters.CharFilter(method='my_custom_filter')
    # def my_custom_filter(self, queryset, name, value):
    #     first_name, last_name = value.split()
    #     return queryset.filter(Q(user__first_name__icontains=first_name) | Q(user__last_name__icontains=last_name))










   