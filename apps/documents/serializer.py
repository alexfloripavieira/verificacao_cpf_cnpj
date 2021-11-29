from rest_framework import  serializers
from .models import DocumentModel
from .service import DocumentsService
_SERVICE = DocumentsService()

#Validações de frontend
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = ("id", "cpf_cnpj")
   
#Validações de backend     
class DocumentAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = (
            "id",
            "cpf_cnpj",
        )

    def update(self, instance, validated_data):
        if not _SERVICE.cpf_cnpj_is_valid(validated_data["cpf_cnpj"]):
            raise serializers.ValidationError("CPF/CNPJ inválido")
        validated_data["cpf_cnpj"] = _SERVICE.clean(validated_data)
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        if not _SERVICE.cpf_cnpj_is_valid(validated_data["cpf_cnpj"]):
            raise serializers.ValidationError("CPF/CNPJ inválido")
        validated_data["cpf_cnpj"] = _SERVICE.clean(validated_data["cpf_cnpj"])
        return super().create(validated_data)