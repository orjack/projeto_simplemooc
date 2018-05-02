from django.shortcuts import render, get_object_or_404

# Create your views here.
from simplemooc.cursos.models import Curso


def index(request):
    cursos = Curso.object.all()
    template = 'curso_index.html'
    contexto = {
        'cursos': cursos
    }
    return render(request, template, contexto)

def details(request, slug):
    course = get_object_or_404(Curso, slug=slug)
    context = {
        'course': course
    }
    template_name = 'curso/details.html'
    return render(request, template_name, context)

