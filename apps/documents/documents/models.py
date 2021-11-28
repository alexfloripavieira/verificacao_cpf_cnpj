from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class DocumentModel(models.Model):

    cpf_cnpj = models.CharField(
        max_length=14,
        unique=True
    )

    def __str__(self) -> str:
        return self.cpf_cnpj