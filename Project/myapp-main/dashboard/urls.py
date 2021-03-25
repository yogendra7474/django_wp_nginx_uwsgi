from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('searchany', views.searchany, name="searchany"),
    path('SearchComp', views.SearchComp, name="SearchComp"),
    path('contact', views.contact, name="contact"),
    path('company', views.company, name="company"),
    # path('dasmain', views.dasmain, name="dasmain"),
    path('Client_top', views.Client_top, name="Client_top"),
    path('Client_acc', views.Client_acc, name="Client_acc"),
    path('Clinet_save', views.Clinet_save, name="Clinet_save"),
    path('SaveSearch', views.SaveSearch, name="SaveSearch"),
    path('reply', views.reply, name="reply"),
    path('SuggestProject', views.SuggestProject, name='SuggestProject'),
    path('Save', views.SaveSearchResult, name='save'),
    path('CompanySave', views.CompanySave, name='CompanySave'),
    path('ContactSave', views.ContactSave, name='ContactSave'),
    path('WindowsLoadData', views.WindowsLoadData, name='WindowsLoadData'),
    path('SaveUpdate',views.SavedSearchUpdate,name='SaveUpdate'),
]


