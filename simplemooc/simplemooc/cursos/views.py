from django.shortcuts import render, get_object_or_404

# Create your views here.
from simplemooc.cursos.forms import ContactCourse
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
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'curso_details.html'
    return render(request, template_name, context)
