from django.urls import path, include 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='usermanagement/login.html'), name='login'),
    path('', auth_views.LoginView.as_view(template_name='usermanagement/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usermanagement/logout.html'), name='logout'),
]