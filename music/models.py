from distutils.command import build
from email.mime import image
from os import name
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


# Composer Table 
class Composer(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    biography = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="Composers/" , default="default.jpg")
    genre = models.CharField(max_length=255,null=True,blank=True)
    nationality = models.CharField(blank=True,null=True,max_length=255)
   
   
    def __str__(self):
        return '{}'.format(self.name)




# Pieces Table
class MasterPiece(models.Model):
    composer = models.ForeignKey(Composer , on_delete=models.CASCADE,null=True)
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tags = TaggableManager()
    song = models.FileField(upload_to="songs/")
 

    def __str__(self):
        return '{}'.format(self.name)
    

class FavoriteComposer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    composer = models.ForeignKey(Composer, on_delete=models.CASCADE)    

    def __str__(self):
        return '{}'.format(self.user)
    

    