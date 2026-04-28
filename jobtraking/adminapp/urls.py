from django.urls import path
from . import views

urlpatterns = [
    path('adminapp/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('users/', views.manage_users, name='manage_users'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),

    path('delete-job/<int:id>/', views.delete_job, name='delete_job'),

    path('logout/', views.admin_logout, name='admin_logout'),
    path('upload-job/', views.upload_job, name='upload_job')
]