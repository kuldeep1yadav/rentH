from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate
from django.views.generic import  CreateView
from django.urls import reverse_lazy

# Create your views here.
from .forms import *
from .models import *




# # def index(request):

# #     return render(request, 'register.html')


# # def hotelowner(request):
# #     return render(request, 'login.html')


class ClientReg(CreateView):
    model = User
    form_class = ClientRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

def loginClient(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('index')  # Redirect to home page after successful login
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class AdminReg(CreateView):
    model = User
    form_class = OwnerRegisterForm
    template_name = 'oregister.html'

def loginAdmin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hotelowner')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'ologin.html',
                  context={'form': AuthenticationForm()})

