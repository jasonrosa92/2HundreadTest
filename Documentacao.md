# Estrutura e Explicação da Aplicação

## Estrutura de Diretórios

├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── jwt.py
│   │   └── utils.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── admin.py
│   └── tests/
│       ├── __init__.py
│       ├── test_routes.py
│       └── test_auth.py
├── .env
├── requirements.txt
└── README.md
└── Documentacao.md
└── Testes.md

### Explicação dos Principais Arquivos e Diretórios

### app/main.py
* Arquivo de entrada principal. Este arquivo inicializa a instância do FastAPI, configura a autenticação via OAuth2, e define as rotas principais da aplicação, incluindo o endpoint /token para autenticação JWT

### app/config.py
* Centraliza as configurações críticas da aplicação, utilizando variáveis de ambiente para segurança e flexibilidade. Este arquivo carrega o SECRET_KEY, ALGORITHM de criptografia e o tempo de expiração dos tokens (ACCESS_TOKEN_EXPIRE_MINUTES), valores essenciais para a criação e validação dos tokens JWT.

### app/db.py
* Simula a camada de banco de dados. Em uma aplicação de produção, essa simulação seria substituída por um sistema de banco de dados real, configurado para realizar a persistência e o gerenciamento seguro dos dados. Esse módulo possibilita testes iniciais sem dependências externas.

### app/auth/jwt.py
* Contém a lógica de criação e verificação de tokens JWT, encapsulando a complexidade da autenticação e garantindo que o sistema possa verificar a identidade do usuário em cada requisição. A função create_access_token gera tokens JWT com informações sobre o usuário e o tempo de expiração, enquanto verify_access_token valida o token recebido, retornando um erro apropriado em caso de falhas.

### app/auth/utils.py
* Utiliza o passlib para operações de hashing de senhas, incluindo as funções verify_password e get_password_hash. O uso do bcrypt garante um nível avançado de segurança, uma vez que senhas não são armazenadas em texto simples e são comparadas por meio de hashes.

### app/routes/user.py
* Define a rota /user, restrita a usuários com o papel user. Este arquivo concentra a lógica de autorização e controle de acesso a conteúdos específicos, garantindo que apenas usuários autenticados e com o papel correto possam visualizar essa rota.

### app/routes/admin.py
* Define a rota /admin, restrita a usuários com o papel admin. Da mesma forma que user.py, este arquivo gerencia a segurança e as permissões de acesso ao conteúdo administrativo, garantindo que apenas administradores autenticados tenham acesso.

### app/tests/test_routes.py
* Testes automatizados para as rotas principais, cobrindo casos de sucesso e de erro. Cada rota é testada com tokens válidos e inválidos, assegurando que as regras de autorização estão sendo seguidas e que os endpoints respondem corretamente conforme o papel do usuário.

### app/tests/test_auth.py
* Testes focados nas funções de autenticação, garantindo que os tokens são criados corretamente e que a verificação de tokens funciona conforme o esperado. Esse módulo é essencial para garantir a integridade da lógica de autenticação da aplicação.

### .env
* Arquivo de variáveis de ambiente. Armazena as configurações sensíveis, como SECRET_KEY e ACCESS_TOKEN_EXPIRE_MINUTES. Esse arquivo não é incluído no controle de versão, evitando exposição acidental de dados sensíveis. É uma prática recomendada em projetos seguros e escaláveis.

### requirements.txt
* Arquivo que lista todas as dependências Python necessárias para rodar a aplicação, como fastapi, jose, e passlib. Facilita a instalação em outros ambientes com o comando pip install -r requirements.txt, garantindo consistência nas bibliotecas utilizadas.


## Fluxo Lógico da Aplicação

* 1  Inicialização: A aplicação inicia no arquivo main.py, que carrega as configurações (config.py) e configura a autenticação JWT usando OAuth2PasswordBearer.

* 2 Autenticação e Autorização: jwt.py lida com a criação e verificação de tokens JWT, enquanto utils.py oferece métodos de hashing para proteger senhas.

* 3 Rotas Protegidas: As rotas são organizadas em routes/, onde user.py e admin.py contêm a lógica de autorização específica para cada papel de usuário.

* 4 Persistência e Simulação de Dados: A camada de "banco de dados" é simulada em db.py, mas é facilmente substituível por um banco de dados real para produção.

* 5 Testes Automatizados: O diretório tests/ garante a confiabilidade e segurança da aplicação, executando testes para as rotas e a autenticação.