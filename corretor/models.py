from django.db import models
#  Create your models here.
class Corretor(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='photos/%d/%m/%Y')
    telefone = models.CharField(max_length=50, blank=True)
    creci = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    descricao = models.TextField( blank=True)

    def __str__(self):
        return self.nome