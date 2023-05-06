from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField(max_length=30)

    def __str__(self):
        return f"{self.name}"
