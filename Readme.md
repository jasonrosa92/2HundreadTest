# Título do projeto

Documentação da API de Autenticação com JWT

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Este projeto é uma API RESTful desenvolvida com FastAPI que implementa autenticação e autorização com JSON Web Tokens (JWT). A API permite a criação de um token JWT para autenticação de usuários, e fornece rotas protegidas com base em permissões de papéis (user e admin).

### 📋 Pré-requisitos

Certifique-se de ter o seguinte instalado antes de prosseguir com a instalação:

    *  Python 3.9+: Instale o Python se ainda não estiver no sistema.
    *  Pip para gerenciar dependências.
    *  Banco de Dados Relacional: SQLite para desenvolvimento local ou PostgreSQL para produção.
    *  Git: Necessário para clonar o repositório. Instale o Git se ainda não estiver disponível.
    *  Virtualenv (opcional): Para criar ambientes virtuais e isolar as dependências. Você pode instalar com o seguinte comando:

```
pip install virtualenv
```

### 🔧 Instalação

### Passo 1: Clonar o Repositório

```
git clone https://github.com/jasonrosa92/2HundreadTest
```

### Passo 2: Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para garantir a separação de dependências:

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```
### Passo 3: Instalar Dependências

Instale todas as dependências necessárias do projeto:

```
pip install -r requirements.txt
```

### Passo 4: Configuração do Banco de Dados

Configure o banco de dados conforme sua necessidade. Para SQLite, o banco será criado automaticamente. Caso esteja utilizando PostgreSQL ou outro banco relacional, defina a URL de conexão no arquivo .env.

- Para SQLite (desenvolvimento):

```
DATABASE_URL=sqlite:///./test.db
```

- Para PostgreSQL (produção):

```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Passo 5: Configuração de Variáveis de Ambiente

Crie o arquivo .env na raiz do projeto para armazenar as configurações sensíveis:

```
SECRET_KEY=seu_secret_key_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./test.db
```
### Nota:
Nunca exponha a SECRET_KEY no código-fonte. Utilize variáveis de ambiente para armazená-la de forma segura.

### Passo 6: Executar a Aplicação
Para rodar a aplicação, utilize o seguinte comando:
```
uvicorn app.main:app --reload
```

## ⚙️ Executando os testes
*  Para visualizar as instruções de teste acesse o arquivo Testes.Md

## 📄 Documentação
* Para visualizar a documentação acesse o arquivo Documentacao.Md

