from django.db import models
from datetime import date

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default = False)
    nome_emprestado = models.CharField(max_length= 30)
    data_emprestado = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    tempo_duracao = models.DateField()

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome