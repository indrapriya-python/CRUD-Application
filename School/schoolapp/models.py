from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)

class Contact(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name =models.CharField(max_length=200)
    Country_name=models.CharField(max_length=100)
    subject = models.TextField()
    