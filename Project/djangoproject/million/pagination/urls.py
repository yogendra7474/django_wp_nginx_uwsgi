from django.urls import path
from pagination import views

urlpatterns = [
    path('', views.pagination_pro, name="pagination_pro"),
    path('pagination_p', views.pagination_p, name="pagination_p"),
]