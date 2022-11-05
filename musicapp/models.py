from django.db import models
from django.core.validators import MinValueValidator

from datetime import date

class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1,'Cannot enter an age value less than 1')])

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=date.today())
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)

    def __str__(self):
        return self.song_id.title
