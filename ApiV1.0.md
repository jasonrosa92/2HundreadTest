# Estrutura de Rotas

## POST /token

* Gera um token JWT para autenticação.

Requisição

``` 
POST /token
Content-Type: application/x-www-form-urlencoded

username=user
password=L0XuwPOdS5U
```

Resposta

``` 
{
  "access_token": "<token_jwt>",
  "token_type": "bearer"
}
```

## GET /user

* Rota protegida, acessível apenas por usuários com o papel "user".p

Requisição
```
GET /user
Authorization: Bearer <token_jwt>
```

Resposta
```
{
  "message": "User content"
}
```

## GET /admin

* Rota protegida, acessível apenas por usuários com o papel "admin".

Requisição
```
GET /admin
Authorization: Bearer <token_jwt>
```

REsṕosta
``` 
{
  "message": "Admin content"
}
```
