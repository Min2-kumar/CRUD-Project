from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField('Name',max_length=70)
    email = models.EmailField('Email',max_length=70)
    password = models.CharField('Password',max_length=70)