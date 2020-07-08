from django.db import models

# Create your models here.
class MusicInfo(models.Model):

    artist = models.CharField(max_length=200, null=True)
    day = models.DateField()
    month = models.DateField()
    year = models.DateField()
    description = models.CharField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return self.artist


