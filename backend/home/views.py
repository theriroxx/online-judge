from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')
