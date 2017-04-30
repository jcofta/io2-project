from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.http import HttpResponse
from .models import Event, Tournament
from django.contrib.auth import models as auth_models

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    context = {}
    return render(request, 'eleague/index.html', context)

def tdetail(request,tournament_id):
    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except Tournament.DoesNotExist:
        raise Http404("Tournament does not exist")
    context = {'tournament':tournament}
    return render(request, 'eleague/tdetail.html', context)

def myevents(request):
    event_list = Event.objects.filter(tournament__owner=request.user)
    context = {'event_list': event_list}
    return render(request, 'eleague/myevents.html',context)

def mytournaments(request):
    tournament_list = Tournament.objects.filter(owner=request.user)
    context = {'tournament_list': tournament_list}
    return render(request, 'eleague/mytournaments.html',context)

#def newtournament(request):
#    context = {}
#    return render(request, 'eleague/newtournament.html',context)

class TournamentCreate(CreateView):
    model = Tournament
    fields =['tag','name','owner','sport']
