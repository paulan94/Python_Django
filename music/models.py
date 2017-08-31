# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
#python manage.py makemigrations music #makes changes
# python manage.py migrate             #applies changes



#Album red has prim key= 1
class Album(models.Model): #creates 4 columns behind the scenes. First class has ID of 1
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField() #url

    def get_absolute_url(self):
        #take to detail view with the pk
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #ondelete, when album is delete, any songs go away too.
    file_type = models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title