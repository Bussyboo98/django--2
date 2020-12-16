from django.shortcuts import render
from django.http import HttpResponse
from frontend.models import *

# Create your views here.
def index(request):
    return  render(request,'frontend/index.html')

def phone(request):
    products=Products.objects.all()
    return  render(request,'frontend/product-list1.html',{'phn':products})

def laptop(request):
    return  render(request,'frontend/product-list2.html')

def detail(request):
    return  render(request,'frontend/product-detail.html')

def about(request):
    about=About.objects.all()
    return render(request, 'frontend/about.html', {'abt': about})


def about_detail(request, abt_id):
    detail = About.objects.get(id = abt_id)
    return render(request, 'frontened/about-detail.html',{'det':detail})

def product_detail(request, phn_id):
    detail = Products.objects.get(id = phn_id)
    return render(request, 'frontened/product-detail.html',{'phn':detail})




def contact(request):
    return render(request, 'frontend/contact.html')
