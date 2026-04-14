from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('applications/', views.my_applications, name='applications'),
    path('analytics/', views.analytics, name='analytics'),
    path('profile/', views.profile, name='profile'),
]