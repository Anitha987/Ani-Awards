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
    image=models.ImageField(upload_to = 'pictures',null= True)
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    post = HTMLField()
    profile=models.ForeignKey(Profile,null= True)
    user=models.ForeignKey(User,blank=True,null=True)
    comments=models.CharField(max_length=30)  

class Review(models.Model):
    RATING_CHOICES = (
        (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),
    )
    project = models.ForeignKey(Project,null=True,blank=True,on_delete=models.CASCADE,related_name="reviews")   
    project = models.ForeignKey(Project,null=True,blank=True,on_delete=models.CASCADE,related_name="reviews")    
    project = models.ForeignKey(Project,null=True,blank=True,on_delete=models.CASCADE,related_name="reviews")
    comment=models.TextField()
    design_rating=models.IntegerField(choices=RATING_CHOICES,default=0) 
    usability_rating=models.IntegerField(choices=RATING_CHOICES,default=0) 
    content_rating=models.IntegerField(choices=RATING_CHOICES,default=0)     
    
    


       
