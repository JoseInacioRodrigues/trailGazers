
# Trilhos 

# -------------------------------
## Python - Django

1-Instalar python

2-Criar virtual environment numa pasta, por exemplo trilhos_venv (não incluir esta pasta no github):
python3 -m venv trilhos_venv

3-Ativar o ambiente para assumir esta configuração por defeito
source trilhos_venv/bin/activate  (linux ou mac)
./trilhos_venv/bin/activate.bat (windows)

4-No repositório do git (trailGazers) e instalar o frameworks django e vários outros módulos
pip install -r requirements.txt 

(poderá ser necessário actualizar o utilitário pip, se for o caso deverá aparecer no terminal uma sugestão nesse sentido)

5-Aceder à pasta trails e colocar o servidor a  correr:
python manage.py runserver 127.0.0.1:8000

6 - user: admin / trails2021

# -------------------------------

O servidor Django disponível no git inclui uma base de dados com duas tabelas - RecursoVideo e RecursoImagem - (core.models)  populados com dois resgistos cada (que podem ser consultados na área de backend).

Tarefa 1.
Criação de uma API (Rest_framework) que permita listar, os recursos com propriedade Activo=True,
Inserir novo recurso (POST), atualizar um recurso (PUT). 
O pedido DELETE não deve remover o recurso mas simplesmente alterar a proriedade Activo para False.

Incluir um token para autenticação do utilizador.


Tarefa 2. 
Backoffice, versão web, que permita autenticar um utilizador (login), consultar, adicionar e remover recursos de video e de imagem.

Framework de desenvolvimento: Vue3 JS


Tarefa 3.
Aplicação para dispositivos móveis android e ios que permita ao utilizador selecionar e visualizar resurso de imagem e de video.

Frameworks de desenvolvimento: Ionic e Vue JS

## -----------------------------------

## Exemplos:

O conteudo da versão base poderá ser acedida através dos seguintes endereços:

http://fmvg.milage.io/admin/  -> backend do django

http://fmvg.milage.io/api/images/  -> api com operações para a tabela de imagens

http://fmvg.milage.io/app/   -> backoffice em vuejs com visualização das imagens devolvidas pela api.

