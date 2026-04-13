from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_job, name='add_job'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
]