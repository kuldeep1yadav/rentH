from django.db import models
# from django.contrib.auth.models import AbstractUser
# # from django.urls import reverse


# class User(AbstractUser):
#     is_owner = models.BooleanField(default=False)
#     is_client = models.BooleanField(default=False)
    

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email=models.EmailField()

# class Owner(models.Model):
#     user = models.OneToOneField(User, related_name='owner', on_delete = models.CASCADE, primary_key = True)
#     def __str__(self):
#             return f'Username: {self.user.username} | First Name: {self.user.first_name} | Lastname: {self.user.last_name}'
    
# class Client(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='client',primary_key = True) 

#     def __str__(self):
#             return f'Username: {self.user.username} | First Name: {self.user.first_name} | Lastname: {self.user.last_name}'
