from django.db import models
from django.utils.timezone import now

# Create your models here.

class Student(models.Model):
    FirstName = models.TextField(max_length=100)
    LastName = models.TextField(max_length=100)
    Email = models.EmailField(unique=True)
    DateOfBirth = models.DateField(null=True)
    Course = models.CharField(max_length=100)
    EnrollmentDate = models.DateField(default=now)