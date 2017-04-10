from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /eleague/
    url(r'^$', views.index, name='index'),
    # # ex: /eleague/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

]
