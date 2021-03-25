from django.urls import path
from search import views

urlpatterns = [
    path('', views.search, name="search"),
    path('Client_top1', views.Client_top, name="Client_top"),
    path('Clinet_save', views.Clinet_save, name="Clinet_save"),
]