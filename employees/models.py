from django.db import models
from users.models import Enterprise


class Employee(models.Model):
    empresa = models.ForeignKey(
        Enterprise,
        related_name="cloths",
        on_delete=models.CASCADE,
    )

    nome = models.CharField(max_length=255)


class Cloth(models.Model):
    empregado = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="roupas"
    )
    tipo = models.CharField(max_length=50)
    tamanho = models.PositiveIntegerField()
    cor = models.CharField(max_length=7)
