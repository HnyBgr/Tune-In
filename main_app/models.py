from django.db import models

# Create your models here.
class MusicInfo(models.Model):

    name = models.CharField(max_length=200)
    date = models.DateField()
    year = models.DateField()
    body = models.CharField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return self.name


