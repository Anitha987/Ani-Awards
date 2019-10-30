from django.test import TestCase
from .models import Profile,Project
# Create your tests here.

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.animal= Project()

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.animal,Project))  

    def test_save_method(self):
        self.animal.save_image()
        images = Project.objects.all() 
        self.assertTrue(len(images)==0)      
    

    def test_update_method(self):
        self.animal.update_image()
        images = Project.objects.filter(id=2).update(image='zebra') 
        self.assertTrue(len(images)==0)   

    def test_delete_method(self):
        self.animal.delete_image()
        images=Project.objects.filter(animal=zebra).delete() 
        self.assertTrue(len(images)==0)     