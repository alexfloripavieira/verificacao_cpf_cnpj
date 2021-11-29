from django.db import models

# Criação do modelo de documento
class DocumentModel(models.Model):

    cpf_cnpj = models.CharField(
        max_length=14,
        unique=True
    )

    def __str__(self) -> str:
        return self.cpf_cnpj