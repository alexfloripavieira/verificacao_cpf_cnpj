from typing import List
from pycpfcnpj import cpfcnpj
from .models import DocumentModel


class DocumentsService():
    def cpf_cnpj_is_valid(self, cpf_cnpj: str) -> bool:
        return cpfcnpj.validate(cpf_cnpj)

    def get_all_documents(self) -> List[DocumentModel]:
        return DocumentModel.objects.all().order_by("-id")

    def clean(self, cpf_cnpj: str) -> str:
        return cpf_cnpj.replace("-", "").replace(".", "").replace("/", "").strip()

    def find_documents_by_cpf_cnpj(self, cpf_cnpj:str) -> List[DocumentModel]:
        return DocumentModel.objects.filter(cpf_cnpj__icontains=cpf_cnpj.strip())

    def delete_by_cpf_cnpj(self, cpf_cnpj:str) -> int:
        return DocumentModel.objects.filter(cpf_cnpj=cpf_cnpj).delete()