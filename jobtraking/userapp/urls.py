from django.urls import path
from django.conf import settings
from . import views

urlpatterns=[
    path('',views.userHome,name="home"),
    path('about/',views.userHome,name="home"),
    path('login/', views.login_view, name='login'),  
    path('login/', views.login_view, name='register'),  # 

]