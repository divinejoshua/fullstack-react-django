from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.home, name='home_page'),              #Register User
    path('user/', views.user, name='user_page'),              #Register User
]