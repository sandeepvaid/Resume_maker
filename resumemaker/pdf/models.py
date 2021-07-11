from django.db import models

class Profile(models.Model):
    name = models.CharField( max_length=200)
    email = models.EmailField(max_length=254)
    summary = models.TextField(max_length=2000)
    experience = models.TextField(max_length=2000)
    phone = models.CharField(max_length=12)
    degree = models.CharField(max_length=200)
    SSC = models.CharField(max_length=200,default='10')
    HSC = models.CharField(max_length=200,default='12')
    university = models.CharField(max_length=200)
    skills = models.CharField(max_length=300)
    github = models.CharField(max_length=300,default='https://github.com/')
    codingprofile = models.CharField(max_length=600,default='')
