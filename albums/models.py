from django.db import models
from genres.models import Genre
from artists.models import Artist
from jwt_auth.models import User

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=50)
    liked = models.CharField(max_length=300)
   
    cover_image = models.CharField(max_length=300)
    genres = models.ManyToManyField('genres.Genre', related_name="albums")
    artist = models.ForeignKey(
        'artists.Artist', related_name="albums",on_delete = models.CASCADE)
    
    owner = models.ForeignKey('jwt_auth.User',related_name = 'albums',on_delete = models.CASCADE)

    #  represent the class objects as a string , add in after

    def __str__(self):
        return f"{self.title}"
 