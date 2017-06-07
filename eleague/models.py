import datetime
from django.utils import timezone

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
        return '../mytournaments'


    def __str__(self):
        return self.name

    def show_tag(self):
        return "This is " + self.tag + " Tournament"

    def get_tag(self):
        return self.tag

    def get_owner(self):
        return self.owner.username

    def get_sport(self):
        return self.sport

    def get_all(self):
        return self.tag + ' ' + self.name + ' ' + self.sport

    def get_all_with_owner(self):
        return self.tag + ' ' + self.name + ' ' + self.owner.username + ' ' + self.sport


class Event(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=500)

    def get_absolute_url(self):
        return '../myevents'


    def __str__(self):
        return self.tournament.tag + " " + str(self.date)

    def get_date(self):
        return str(self.date)

    def get_place(self):
        return self.place
