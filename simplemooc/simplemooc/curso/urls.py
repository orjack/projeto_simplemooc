from django.conf.urls import include, url

from simplemooc.simplemooc.curso.views import index

urlpatterns = [
    url('', index, name='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
 #   url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),
]