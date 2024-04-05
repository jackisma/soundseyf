from django.db import models
from taggit.managers import TaggableManager


class MasterPieces(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    Composer = models.CharField(max_length=255)
    tags = TaggableManager()
    image = models.ImageField(upload_to="songs/",default="songs/default.jpg")
    song = models.FileField(upload_to="songs/")
 

    def __str__(self):
        return '{}'.format(self.name)