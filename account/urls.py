from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
