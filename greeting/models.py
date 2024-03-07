from django.db import models

# Create your models here.
class addshow(models.Model):
    title = models.CharField(max_length=255)
    # file = models.FileField()
    release_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    screen = models.CharField(max_length=25)
    director = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class signup(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255) 

class login(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255) 


    
