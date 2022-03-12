from statistics import mode
from django.db import models

# Create your models here.
class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

class Contact(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Query = models.CharField(max_length=100)