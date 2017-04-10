import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import models as auth_models


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
    def __str__(self):
        return self.tag

class Event(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    date = models.DateTimeField()
    place = models.CharField(max_length=500)
    def __str__(self):
        return self.tournament.tag + " " + self.date
