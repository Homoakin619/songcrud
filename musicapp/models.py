from django.db import models
from django.core.validators import MinValueValidator

from datetime import date

class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1,'Cannot enter an age value less than 1')])

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=date.today())
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste,on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)
