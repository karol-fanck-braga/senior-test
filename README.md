
# API de gerenciamento de tarefas 

  

Este é um projeto de uma API de gerenciamento de tarefas desenvolvida utilizando Django REST Framework.

  

## Dependências

 
Certifique-se de ter instalado os seguintes pacotes:

  
- Django

- Django REST Framework

- Django REST Framework SimpleJWT

- Django Filters

  

Você pode instalar todas as dependências usando o comando:

  

    pip install -r requirements.txt

  

# Configuração

  

Execute as migrações do banco de dados:

  

    python manage.py migrate

  

Crie migrações para quaisquer alterações nos modelos:

  

    python manage.py makemigrations

  

# Endpoints

  

**GET** /api/tasks: Retorna uma lista de todas as tarefas.

**GET** /api/tasks/{id}: Retorna uma tarefa específica com o ID fornecido.

**POST** /api/tasks: Cria uma nova tarefa. Envie os dados da tarefa no corpo da solicitação.

**PUT** /api/tasks/{id}: Atualiza completamente uma tarefa existente com o ID fornecido. Envie todos os campos da tarefa no corpo da solicitação.

**PATCH** /api/tasks/{id}: Atualiza parcialmente uma tarefa existente com o ID fornecido. Envie apenas os campos que deseja atualizar no corpo da solicitação.

**DELETE** /api/tasks/{id}: Remove a tarefa com o ID fornecido.

  

Certifique-se de incluir o token JWT de autenticação no cabeçalho da solicitação.

**POST** /token/: Gera um token de acesso.
