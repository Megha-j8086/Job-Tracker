from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_job, name='add_job'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
    path('jobs/', views.jobs_list, name='jobs'),
    path('applications/', views.applications, name='applications'),
    path('apply-job/<int:id>/', views.apply_job, name='apply_job'),
    path('delete-application/<int:id>/', views.delete_application, name='delete_application'),

]