from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.documents.models import DocumentModel

from .serializer import DocumentSerializer
from .service import DocumentsService

_SERVICE = DocumentsService()


def home(request):
    if request.POST and request.POST['action'] == "Adicionar":
        if not _SERVICE.cpf_cnpj_is_valid(request.POST.get("cpf_cnpj")):
            messages.error(request, 'Campo CPF/CNPJ é inválido')
        else:
            data = {
                "cpf_cnpj":  _SERVICE.clean(request.POST["cpf_cnpj"])
            }
            serializer = DocumentSerializer(data=data)
            if not serializer.is_valid():
                messages.error(request, "CPF/CNPJ já existente")
            else:
                serializer.save()
                messages.success(request, 'Registro Salvo com Sucesso')

        documents = _SERVICE.get_all_documents()
        paginator = Paginator(documents, 5)
        page = request.GET.get('p')
        documents = paginator.get_page(page)
        return render(request, "dash.html", context={"documents": documents})
    elif request.POST and request.POST['action'] == "Excluir":
        _SERVICE.delete_by_cpf_cnpj(request.POST and request.POST['cpf_cnpj'])
        documents = _SERVICE.get_all_documents()
        paginator = Paginator(documents, 5)
        page = request.GET.get('p')
        documents = paginator.get_page(page)
        messages.info(request, 'Registro Excluido com sucesso')
        return render(request, "dash.html", context={"documents": documents})

    if request.POST.get('cpf_cnpj') is not None:
        documents = _SERVICE.find_documents_by_cpf_cnpj(
            request.POST.get('cpf_cnpj'))
    else:
        documents = _SERVICE.get_all_documents()
    paginator = Paginator(documents, 5)
    page = request.GET.get('p')
    documents = paginator.get_page(page)
    return render(request, "dash.html", context={"documents": documents})


class DocumentsView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = DocumentModel.objects.all()
    http_method_names = ['post', 'get']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        "cpf_cnpj",
    )

    def create(self, request, *args, **kwargs):
        if not _SERVICE.cpf_cnpj_is_valid(request.data):
            return Response(
                {"message": "CPF/CNPJ inválido"},
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json")
        request.data["cpf_cnpj"] = _SERVICE.clean(request.data["cpf_cnpj"])
        return super().create(request, *args, **kwargs)
