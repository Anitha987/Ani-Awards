from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photos',null=True,blank=True)
    biography=models.TextField(max_length=60)
    project=models.CharField(max_length=30)

    def __str__(self):
        return self.biography

class Project(models.Model):
    image=models.ImageField(upload_to = 'pictures',null= True)
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=30) 
    post = HTMLField()
    profile=models.ForeignKey(Profile,null= True)
    user=models.ForeignKey(User,blank=True,null=True)
    comments=models.CharField(max_length=30)  

    return title      
