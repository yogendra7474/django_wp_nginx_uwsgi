from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.accounts, name="accounts"),
#     path('guest', views.guest, name="guest"),
#     path('signup', views.signup, name="signup"),
#     path('forgot', views.forgot, name="forgot"),
#     path('RequestDemo', views.demo, name="RequestDemo"),
#     # path('signup', views.signup, name="signup"),
#     # path('login', views.login, name="login"),
#     # path('changepass', views.changepass, name="changepass"),
#     # path('activate/<uidb64>/<token>', views.activate, name="activate"),

# 
]