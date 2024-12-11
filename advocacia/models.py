from django.db import models

class Advogado(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome

class Caso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_abertura = models.DateField()
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE, related_name='casos')

    def __str__(self):
        return self.titulo
