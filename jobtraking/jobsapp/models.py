from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')  
    user_id = models.IntegerField()
    