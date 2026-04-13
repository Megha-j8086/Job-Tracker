from django.db import models

# Create your models here.
class Job(models.Model):
    user_id = models.IntegerField()
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    