from django.shortcuts import render, redirect
from . import admin


# def register(request):
#     return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def property(request):
    return render(request, 'property-grid.html')
    
# def login(request):
#     return render(request, 'login.html')

# def ologin(request):
#     return render(request, 'ologin.html')



# def oregister(request):
#     return render(request, 'oregister.html')

def propertysingle(request):
    return render(request, 'property-single.html')

def blog(request):
    return render(request, 'blog-grid.html')

def singleblog(request):
    return render(request, 'blog-single.html')

def hotelowner(request):
    return render(request, 'hotelowner.html')

def about(request):
    return render(request, 'about.html')




# # User Registration View
# def user_register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Redirect to home page after registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/user_register.html', {'form': form})

# # User Login View
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')  # Redirect to home page after login
#         else:
#             # Handle invalid login
#             return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
#     else:
#         return render(request, 'registration/login.html')



# def user_register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to user dashboard or home page
#             return redirect('index')
#     return render(request, 'login.html')

# def owner_register(request):
#     if request.method == 'POST':
#         form = OwnerRegistrationForm(request.POST)
#         if form.is_valid():
#             owner = form.save(commit=False)
#             owner.user = request.user
#             owner.save()
#             return redirect('ologin')
#     else:
#         form = OwnerRegistrationForm()
#     return render(request, 'oregister.html', {'form': form})

# # Owner login view (similar to user_login)
# def owner_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to user dashboard or home page
#             return redirect('/')
#     return render(request, 'ologin.html')