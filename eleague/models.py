import datetime

from django.db import models
from django.contrib.auth import models as auth_models
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class Tournament(models.Model):
    tag = models.CharField(max_length=200,blank=False,unique=True)
    name = models.CharField(max_length=300)
    owner = models.ForeignKey(auth_models.User,on_delete=models.CASCADE)
    SPORTS = (
    ('BAD','Badminton'),
    ('TEN','Tenis'),
    ('VOL','Volleyball'),
    ('PIN','Pingpong')
    )
    sport = models.CharField(max_length=3,choices=SPORTS)

    def get_absolute_url(self):
        return reverse('mytournaments',kwargs={'pk':self.pk})


    def __str__(self):
        return self.name

class Event(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    date = models.DateTimeField()
    place = models.CharField(max_length=500)
    def __str__(self):
        return self.tournament.tag + " " + str(self.date)
