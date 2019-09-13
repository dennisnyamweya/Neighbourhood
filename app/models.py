from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hood(models.Model):
    # admin = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    count = models.IntegerField()
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.name
    
    
class Business(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100,default='location')
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.name
    
    
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name