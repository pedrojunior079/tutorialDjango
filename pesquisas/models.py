import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=200)
    pub_data = models.DateTimeField("data de publicação")
    
    def __str__(self):
        return self.pergunta_texto

    def foi_publicado_recentemente(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.escolha_texto	
