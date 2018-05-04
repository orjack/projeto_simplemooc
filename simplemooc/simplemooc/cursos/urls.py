from django.conf.urls import url
from django.urls import path
from cursos.views import details
from simplemooc.cursos.views import index

urlpatterns = [
    path('', index, name='index'),
#    path('<pk>/', details, name='detail'),
#    path('<slug>/', details, name='detail'),
#    url(r'^(?P<pk>\d+)/$', details, name='detail'),
    url(r'^(?P<slug>[\w_-]+)/$', details, name='detail'),
]
