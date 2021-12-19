from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    mobileNo = models.IntegerField()
    email = models.CharField(max_length=30)
    age = models.IntegerField()
    education = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    university = models.CharField(max_length=30)
    insti = models.CharField(max_length=30)
    yop = models.CharField(max_length=30)
    percentage = models.CharField(max_length=30)

