from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.http import HttpResponse
from .models import Event, Tournament
from django.contrib.auth import models as auth_models




def index(request):
    context = {}
    return render(request, 'eleague/index.html', context)

def myevents(request):
    event_list = Event.objects.filter(tournament__owner=request.user)
    context = {'event_list': event_list}
    return render(request, 'eleague/myevents.html',context)

def mytournaments(request):
    tournament_list = Tournament.objects.filter(owner=request.user)
    context = {'tournament_list': tournament_list}
    return render(request, 'eleague/mytournaments.html',context)
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
