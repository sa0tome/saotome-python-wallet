# `saotome-python-wallet`

É um repositório para solucionar o [challenge](https://github.com/MaisTodos/backend-python-wallet) proposto pela MaisTodos.

# Como rodar o projeto

```sh

pipenv shell
pipenv install
export FLASK_APP=cashback
export FLASK_ENV=development
export FLASK_DEBUG=True
flask run

```
## Iniciar o database

```sh

flask db migrate
flask db upgrade

```

# Ferramentas

- pipenv

Gerenciador de pacotes pip com virtual env automático

- Flask, flask-marshmallow, marshmallow-sqlalchemy

Respectivamente: web framework para Python, biblioteca de serialização e deserialização e ORM

- Vim

Editor de texto 

- Postman 

Para testar as requisições
