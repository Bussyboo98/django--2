from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('<h1> Login page</h1>')
def dashboard(request):
    return HttpResponse('<h1> Dashboard page</h1>')