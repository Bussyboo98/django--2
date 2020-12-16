from django.shortcuts import render, redirect


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from backend.models import *

# Create your views here.

def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'backend/login.html')

@login_required(login_url ='/dashboard')
def dashboard(request):
    return render(request, 'backend/admin.html')

def list1(request):
    return  render(request,'backend/view-products.html')

def category(request):
    category=Category.objects.all()
    return  render(request,'backend/category.html', {'phn':category})

    
@login_required(login_url ='/dashboard')
def confirm_logout(request):
    return render(request, 'backend/confirm-logout.html')

@login_required(login_url ='/dashboard')
def logout_view(request):
    return redirect('backend:logout_view')

