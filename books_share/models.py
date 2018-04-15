from django.db import models

class Book(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30, verbose_name='Título')
    author = models.CharField(max_length=30, verbose_name='Autor')
    description = models.TextField('Descrição', blank=True)
    edition = models.IntegerField(verbose_name='Edicao')
    year = models.CharField(max_length=4, verbose_name='Ano')
    image = models.ImageField(
        upload_to='book/images', verbose_name='Imagem',
        null=True, blank=True
    )
