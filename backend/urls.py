from django.urls import path
from backend import views


app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
    path('list1-page/', views.list1, name='list1'),
    path('category-page/', views.category, name='category'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout_view/', views.logout_view, name='logout_view')
]
    
