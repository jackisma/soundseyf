from distutils.command import build
from doctest import BLANKLINE_MARKER
from email.mime import image
from os import name
from django.db import models
from taggit.managers import TaggableManager


class Composer(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    biography = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="Composers/" , default="default.jpg")
    genre = models.CharField(max_length=255,null=True,blank=True)
   
   
    def __str__(self):
        return '{}'.format(self.name)





class MasterPiece(models.Model):
    composer = models.ForeignKey(Composer , on_delete=models.CASCADE,null=True)
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tags = TaggableManager()
    song = models.FileField(upload_to="songs/")
 

    def __str__(self):
        return '{}'.format(self.name)