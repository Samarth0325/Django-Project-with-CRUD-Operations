from django.db import models

# Create your models here.
class User(models.Model): #we create a class of user.which go on admin page where we call it.
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)