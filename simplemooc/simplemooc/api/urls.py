from django.urls import path
from api.views import home, contato

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
]
