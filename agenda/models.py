from django.db import models

# Create your models here.


class Agenda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data e hora do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação')

    class Meta:
        db_table = 'agenda'
