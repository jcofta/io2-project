from django.conf.urls import url
from . import views

app_name = 'eleague'

urlpatterns = [
    # ex: /eleague/
    url(r'^$', views.index, name='index'),
    # # ex: /eleague/5/
    url(r'^(?P<tournament_id>[0-9]+)$',views.tdetail,name='tdetail'),
    #url(r'^(?P<tournament_id>[0-9]+)/newevent/$',views.EventCreate.as_view(), name='newevent'),
    url(r'^([0-9]+)/(?P<event_id>[0-9]+)$',views.edetail,name='edetail'),
    url(r'^myevents/$',views.myevents, name='myevents'),
    url(r'^mytournaments/$',views.mytournaments, name='mytournaments'),
    url(r'^newtournament/$',views.TournamentCreate.as_view(), name='newtournament'),
    url(r'^newevent/$',views.EventCreate.as_view(), name='newevent')

]
