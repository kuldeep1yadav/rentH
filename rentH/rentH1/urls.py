from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'), 
    path('property-grid.html', views.property, name='property'),
    path('property-single.html', views.propertysingle, name='propertysingle'),
    # path('login.html', views.user_login, name='login'),
    # path('register.html', views.user_register, name='register'),
    # path('ologin.html', views.owner_login, name='ologin'),
    # path('oregister.html', views.owner_register, name='ownerregister'), 
    # path('user/register/', views.user_register, name='user_register'),
    # path('user/login/', views.user_login, name='user_login'),
    # path('owner/register/', views.owner_register, name='owner_register'),
    # path('owner/login/', views.owner_login, name='owner_login'),
    path('blog-grid.html', views.blog, name='blog'),
    path('blog-single.html', views.singleblog, name='singleblog'),
    path('hotelowner.html', views.hotelowner, name='hotelowner'),  
]
