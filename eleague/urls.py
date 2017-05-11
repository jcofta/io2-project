from django.conf.urls import url
from . import views

app_name = 'eleague'

urlpatterns = [
    # ex: /eleague/
    url(r'^$', views.index, name='index'),
    # ex: /eleague/5/
    url(r'^(?P<tournament_id>[0-9]+)/$',views.tdetail,name='tdetail'),
    # ex: /eleague/5/6
    url(r'^([0-9]+)/(?P<event_id>[0-9]+)/$',views.edetail,name='edetail'),
    # ex: /eleague/myevents
    url(r'^myevents/$',views.myevents, name='myevents'),
    # ex: /eleague/mytournaments
    url(r'^mytournaments/$',views.mytournaments, name='mytournaments'),
    # ex: /eleague/newtournament
    url(r'^newtournament/$',views.TournamentCreate.as_view(), name='newtournament'),
    # ex: /eleague/newevent
    url(r'^newevent/$',views.EventCreate.as_view(), name='newevent'),
    # ex: /eleague/<tournament_tag>/search
    url(r'^search/$',views.search,name='search')


]
