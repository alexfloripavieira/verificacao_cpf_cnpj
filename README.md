Primeiro:

'docker run --name darth-vader-postgres -p 5432:5432 -e POSTGRES_PASSWORD='postgres' -d postgres:10-alpine'

docker stop $(docker ps -aq); docker rm $(docker ps -aq)

Segundo:
'python -m venv venv'

Terceiro
Na raiz do projeto
'venv/Scripts/activate'
'pip install -r requirements.txt'
'python manage.py migrate'

Quarto
'python manage.py runserver'
