#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
	titulo = models.CharField(max_length=100, verbose_name='Título de la Noticia', unique=True)
	ingredientes = models.TextField(verbose_name='Noticia', help_text='Redacta una breve descripcion de los acontecimientos ')
	preparacion = models.TextField(verbose_name='Lugar de los hechos', help_text='lugar donde sucedieron los hechos')
	imagen = models.ImageField(upload_to='recetas', verbose_name='Noticia')
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text='Tu comentario', verbose_name='Comentario')

    def __unicode__(self):
        return self.texto
