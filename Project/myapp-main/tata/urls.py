from django.urls import path
from tata import views

urlpatterns = [
    path('', views.tata, name="tata"),
    path('pix', views.pix, name="pix"),
    path('reply', views.reply, name="reply"),
]