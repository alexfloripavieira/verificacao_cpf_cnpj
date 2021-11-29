import pytest
import json

#Teste resposta da pagina inicial
@pytest.mark.django_db
def test_initial_page(client):

    response = client.get('/')
    assert response.status_code == 200
    
#Teste create pagina inicial
@pytest.mark.django_db
def test_initial_page_create(client):

    data = {
        "cpf_cnpj": "980.680.000-11",
        "action":"Adicionar"
    }

    response = client.post('/', data=data)
    assert response.status_code == 200

#Teste get list da API
@pytest.mark.django_db
def test_get_documents_list_api(client):

    response = client.get('/api/documents/')

    assert response.status_code == 200
    assert response.json() == []

#Teste create API
@pytest.mark.django_db
def test_create_documents_api(client):
    data = {
        "cpf_cnpj": "980.680.000-11",
       }

    response = client.post('/api/documents/', data=data)

    data_compare = {
        'id': 2,
        'cpf_cnpj': '98068000011',
    }

    assert response.status_code == 201
    assert response.json() == data_compare

#Teste validação informações invalidas
@pytest.mark.django_db
def test_create_documents_api_invalid_data(client):
    data = {
      
    }

    response = client.post('/api/documents/', data=data)

    data_compare = {
        'cpf_cnpj':[ 'Este campo é obrigatório.']}
    

    assert response.status_code == 400
    assert response.json() == data_compare

#Teste de id invalido
@pytest.mark.django_db
def test_update_documents_api_invalid_id(client):
    data = {
        'cpf_cnpj': '98068000011',
    }

    response = client.patch('/api/documents/1/', data=data)

    data_compare = {
        "detail": "Não encontrado."
    }

    assert response.status_code == 404
    assert response.json() == data_compare
