# views.py in auth app
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "User created and logged in successfully")
            return redirect('/')  # Redirect to the home page
        else:
            messages.error(request, "User creation failed")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful')
            return redirect('/')  # Redirect to the home page
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.info(request, 'Logout successful')
    return redirect('/auth/login/')
