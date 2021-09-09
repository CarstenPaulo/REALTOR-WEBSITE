from django.db import models
from datetime import datetime
from corretor.models import Corretor
from embed_video.fields import EmbedVideoField

# Create your models here.
class Listagen(models.Model):
    Corretor = models.ForeignKey(Corretor, on_delete=models.DO_NOTHING,)
    tipo_imovel = (
        ('Casa', 'Casa'),
        ('Chácara', 'Chácara'),
        ('Fazenda', 'Fazenda'),
        ('Lote', 'Lote'),
        ('Sítio', 'Sítio'),
        ('Terreno', 'Terreno'),
    )
    tipo_de_imovel = models.CharField(max_length=100,choices=tipo_imovel)
    titulo = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.IntegerField()
    quartos = models.IntegerField(blank=True, null=True)
    banheiro = models.IntegerField(blank=True, null=True)
    garagem = models.IntegerField(blank=True, null=True)
    hectares = models.IntegerField()
    metrosquadrados = models.IntegerField()
    foto_principal = models.ImageField(upload_to='photos/%d/%m/%Y/')
    foto_1 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_2 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_3 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_4 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_5 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_6 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_7 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_8 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_9 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    foto_10 = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    publicado = models.BooleanField(default=True)
    data_listada = models.DateTimeField(default=datetime.now, blank=True)
    video1 = EmbedVideoField(blank=True)
    video2 = EmbedVideoField(blank=True)
 

    def __str__(self):
        return self.titulo

    


