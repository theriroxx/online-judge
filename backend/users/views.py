# views.py in auth app
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.save()
            messages.info(request,"User created successfully")
            return redirect("/auth/login/")
        
        messages.info(request,'User with the username exists')
        return redirect("/auth/register/")
    return render(request, 'register.html')

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
