from django.conf.urls import include, url

from simplemooc.simplemooc.core.views import contact, home

urlpatterns = [
    url('', home, name='home'),
    url('contato/', contact, name='contact'),
]