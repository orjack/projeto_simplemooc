from django.db import models


# Create your models here.
class CursoManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(descricao__icontains=query)
        )


class Curso(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    slug = models.SlugField(verbose_name='Atalho')
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    about = models.TextField(verbose_name='Sobre', blank=True)
    data_inicio = models.DateField(verbose_name='Data de Inicio', blank=True, null=True)
    imagem = models.ImageField(verbose_name='Imagem', upload_to='imagens', null=True, blank=True)
    data_criacao = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    data_atualizacao = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)
    object = CursoManager()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']
