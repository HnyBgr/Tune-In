from django.db import models

# Create your models here.
class MusicInfo(models.Model):

    artist = models.CharField(max_length=200, null=True)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    description = models.TextField()
    band = models.CharField(max_length=200)

    def __str__(self):
        return self.artist


