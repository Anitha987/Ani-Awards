from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photos',null=True,blank=True)
    biography=models.TextField(max_length=60)
    

    def __str__(self):
        return self.biography

class Project(models.Model):
    image=models.ImageField(upload_to ='pictures')
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=60)
    link=models.URLField(max_length=200,db_index=True,unique=True,null=True)
    post = HTMLField()
    profile=models.ForeignKey(Profile,null= True,on_delete=models.CASCADE)
    design=models.IntegerField(choices=list(zip(range(0,10),range(0,10))),default=0)
    content=models.IntegerField(choices=list(zip(range(0,10),range(0,10))),default=0)
    usability=models.IntegerField(choices=list(zip(range(0,10),range(0,10))),default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    comments=models.CharField(max_length=30) 

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images 
       






    
    


       
