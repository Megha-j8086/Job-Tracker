from django.db import models

# Create your models here.
class Add_Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    experience = models.IntegerField()
    job_type = models.CharField(max_length=50)
    skills = models.CharField(max_length=200)
    description = models.TextField()

