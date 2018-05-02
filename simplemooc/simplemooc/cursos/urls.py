from django.urls import path
from simplemooc.cursos.views import index

urlpatterns = [
    path('', index, name='index'),
]
