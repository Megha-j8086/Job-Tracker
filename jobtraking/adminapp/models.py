from django.db import models

class Add_Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    salary = models.IntegerField()
    experience = models.IntegerField()
    job_type = models.CharField(max_length=50)
    skills = models.CharField(max_length=300)
    description = models.TextField()

 