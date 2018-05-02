from django.shortcuts import render


def home(request):
    template = 'home.html'
    return render(request, template)


def contact(request):
    return render(request, 'contact.html')