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

## Auth

Foi feita usando a codificação `base64`. 

```sh
export WALLET_SECRET="sua_chave_segura"
```
Ao realizar a requisição para API, adicione no cabeçalho a chave codificada com base64:

`Authorization:Token <token_sua_chave_segura>`

### Exemplo

```sh
export WALLET_SECRET="banana"
curl --header "Authorization:Token YmFuYW5hy5" --url https://localhost:5000/api/cashback --request POST --data '{"foo": "bar"}'
```

# Ferramentas

- pipenv

Gerenciador de pacotes pip com virtual env automático

- Flask, flask-marshmallow, marshmallow-sqlalchemy

Respectivamente: web framework para Python, biblioteca de serialização e deserialização e ORM

- requests

Biblioteca para Python para enviar requisições

- Vim

Editor de texto 

- Postman 

Para testar as requisições
