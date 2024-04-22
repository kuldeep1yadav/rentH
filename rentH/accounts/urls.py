from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import ClientReg
from accounts.views import AdminReg

from . import views

urlpatterns = [
    path('register/', ClientReg.as_view(), name='register'),
    path('login/', views.loginClient, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('oregister/', AdminReg.as_view(), name='oregister'),
    path('ologin/', views.loginAdmin, name='ologin'),

    # path('profile/', views.profile, name= 'profile'),


]
