from django.db import models
from albums.models import Album
from jwt_auth.models import User

# Create your models here.

class Comment(models.Model):

    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(
        "albums.Album",  # this defines where the relationship is - in the shows app on the Show model
        related_name="comments",  # This is what the column will be called on the show lookup
        # This specifies that the comment should be deleted if the show is deleted
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        "jwt_auth.User",
        related_name="comments",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.text}"
   