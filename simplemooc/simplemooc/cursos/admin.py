from django.contrib import admin

# Register your models here.
from simplemooc.cursos.models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'data_inicio']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug': ['nome']}

admin.site.register(Curso, CursoAdmin )