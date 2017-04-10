from django.contrib import admin

# Register your models here.

from .models import Tournament, Event

admin.site.register(Tournament)
admin.site.register(Event)
