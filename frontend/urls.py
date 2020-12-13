from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('detail/<int:abt_id>/', views.about_detail, name = 'about_detail'),
    path('contact-page/', views.contact, name='contact'),  
    path('phone-page/', views.phone, name='product-list1'), 
    path('laptop-page/', views.laptop, name='product-list2'), 
    path('detail-page/', views.detail, name='product-detail'), 
]