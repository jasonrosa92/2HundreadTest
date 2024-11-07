# Como Realizar os testes:

## Para realizar os testes com Pytest:

*  Navegue até o diretório de App e rode o seguinte comando:

```
pytest tests
```
Esse comando ira rodar todos os testes.

## Para realizar os testes com Postman:

### Passo 1 Testar a Rota de Login (/token)

* 1 A primeira coisa que você precisa fazer é obter o token JWT chamando o endpoint /token com as credenciais de um dos usuários fictícios (como user ou admin).

* 2 Configuração da Requisição no Postman:
    - 1 Abra o Postman.
    - 2 Crie uma nova requisição:
        * Método: POST
        * URL: http://localhost:8000/token
        * Na aba "Body", selecione x-www-form-urlencoded e adicione as seguintes chaves e valores:
            - Key: username — Value: user (ou admin se for testar com o administrador)
            - Key: password — Value: L0XuwPOdS5U (ou JKSipm0YH para o admin)
    - 3 Envie a requisição.
    - 4 Se as credenciais estiverem corretas, você deverá receber uma resposta similar a esta:
        ```
        {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "token_type": "bearer"
        } 
        ```
    - 5 Copie o valor do access_token (o token JWT gerado).

### Passo 2: Testar a Rota Protegida /user

* Agora que você tem o token JWT, pode usar esse token para acessar a rota protegida /user.
* Configuração da Requisição no Postman:
    - Crie uma nova requisição:
        * Método: GET
        * URL: http://localhost:8000/user
        * Na aba "Headers", adicione o seguinte cabeçalho:
            - Key: Authorization — Value: Bearer <access_token>, onde <access_token> é o token que você copiou da resposta anterior.
        * Envie a requisição.
        * Se o token for válido e o usuário tiver o papel adequado (no caso user), você verá a resposta:
            - ``` 
            {
                "message": "User content"
                }
            ```
* Se o token não for válido ou o usuário não tiver o papel correto, você verá um erro de 403 Forbidden.

### Passo 3: Testar a Rota Protegida /admin

* Da mesma forma, você pode testar a rota protegida /admin, mas agora apenas um usuário com o papel admin poderá acessar.
* Configuração da Requisição no Postman:
    * 1 Crie uma nova requisição:
        - Método: GET
        - URL: http://localhost:8000/admin
        - Na aba "Headers", adicione o seguinte cabeçalho:
            * Key: Authorization — Value: Bearer <access_token>, onde <access_token> é o token que você copiou da resposta do login para o usuário admin (se estiver testando como admin).
    * 2 Envie a requisição.
    * 3 Se o token for válido e o usuário tiver o papel adequado (no caso admin), você verá a resposta:
        ``` 
        {
                "message": "Admin content"
            }
        ```
    * 4 Se o token não for válido ou o usuário não for admin, você verá um erro de 403 Forbidden.

