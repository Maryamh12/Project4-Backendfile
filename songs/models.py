from django.db import models
from albums.models import Album


# Create your models here.

class Song(models.Model):

    name = models.CharField(max_length=300)
    url_voice = models.CharField(max_length=300)
    
    album = models.ForeignKey(
        "albums.Album",  # this defines where the relationship is - in the shows app on the Show model
        related_name="songs",  # This is what the column will be called on the show lookup
        # This specifies that the comment should be deleted if the show is deleted
        on_delete=models.CASCADE
    )
   
    def __str__(self):
        return f"{self.name}"
   
