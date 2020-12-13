from django.shortcuts import render
from django.http import HttpResponse
from frontend.models import *

# Create your views here.
def index(request):
    return  render(request,'frontend/index.html')

def phone(request):
    return  render(request,'frontend/product-list1.html')

def laptop(request):
    return  render(request,'frontend/product-list2.html')

def detail(request):
    return  render(request,'frontend/product-detail.html')

def about(request):
    about=About.objects.all()
    return render(request, 'frontend/about.html', {'abt': about})


def about_detail(request, abt_id):
    detail = About.objects.get(id = abt_id)
    return render(request, 'frontened/detail.html',{'det':detail})




def contact(request):
    return render(request, 'frontend/contact.html')
