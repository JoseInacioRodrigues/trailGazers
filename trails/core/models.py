from django.db import models

# Create your models here.

class Recurso(models.Model):

    pass


class RecursoVideo(models.Model):
    data_criacao = models.DateField(auto_now_add=True)
    video = models.FileField(upload_to='videos', default=None)
    descricao = models.TextField(default='')
    activo = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'videos'  
        verbose_name_plural = "RecursosVideo" 

    def __str__(self):
        return self.descricao 


class RecursoImagem(models.Model):
    data_criacao = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens',default=None)
    descricao = models.TextField(default='')
    activo = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'imagens' 
        verbose_name_plural = "RecursosImagem"

    def __str__(self):
        return self.descricao 
