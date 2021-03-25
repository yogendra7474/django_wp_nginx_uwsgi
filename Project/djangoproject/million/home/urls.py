from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('forgot', views.forgot, name="forgot"),
    path('guest', views.guest, name="guest"),
    path('SignupPage', views.SignupPage, name="SignupPage"),
    path('signup', views.signup, name="signup"),
    path('profile', views.profile, name="profile"),
    path('RequestDemo', views.demo, name="RequestDemo"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),
    path('forgot_pass', views.forgot_pass, name="forgot_pass"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('verifyUserAccount/<uidb64>/<token>', views.verifyUserAccount, name="verify"),
    path('password_reset/<uidb64>/<token>', views.password_reset, name="password_reset"),
    path('password_set/<uidb64>/<token>', views.password_set, name="password_set"),
]