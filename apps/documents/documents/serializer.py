from rest_framework import fields, serializers

from .models import DocumentModel

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = ("id", "cpf_cnpj")
        extra_kwargs = {"username": {"error_messages": {"unique": "Registro ja existente"}}}
        error_messages = {"cpf_cnpj": "Registro ja existente"}