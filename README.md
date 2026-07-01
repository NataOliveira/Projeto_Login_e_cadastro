# 🏦 Dreyfus Bank — Sistema de Login e Cadastro

Aplicação desktop desenvolvida em **Python** com **CustomTkinter**, que simula um sistema bancário simples de autenticação e cadastro de clientes, com persistência em banco de dados relacional e senhas protegidas por hash.

## 📋 Sobre o projeto

O sistema permite que um usuário se cadastre informando dados pessoais e de endereço, realize login com validação segura de senha (via `bcrypt`) e visualize suas informações cadastrais em uma tela inicial após a autenticação.

## ✨ Funcionalidades

- **Tela de Login** com validação de usuário e senha
- **Cadastro de novos usuários**, com os campos:
  - Usuário e nome completo
  - Senha (armazenada com hash `bcrypt`)
  - CPF, e-mail e telefone
  - Data de nascimento (com validação de formato `DD/MM/AAAA`)
  - Endereço completo (logradouro, número, bairro, cidade, estado via `ComboBox` e CEP)
- **Validação de campos obrigatórios** antes de salvar o cadastro
- **Tela inicial (home)** exibindo os dados do cliente autenticado
- Tratamento de erros de conexão com o banco (mensagem de "Sistema offline")
- Interface gráfica construída com **CustomTkinter**, com suporte a modo claro/escuro

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — interface gráfica
- [bcrypt](https://pypi.org/project/bcrypt/) — hash de senhas
- [Pillow (PIL)](https://pypi.org/project/pillow/) — manipulação de imagens
- [PostgreSQL](https://www.postgresql.org/) — banco de dados relacional
- [psycopg](https://www.psycopg.org/) — driver de conexão com o PostgreSQL
- [python-dotenv](https://pypi.org/project/python-dotenv/) — carregamento de variáveis de ambiente

## 📁 Estrutura esperada do projeto

```
projeto/
├── main.py                 # Arquivo principal (código da aplicação)
├── conexao_db.py            # Módulo com as funções conectar_banco() e encerrar_conectar_banco()
├── .env                       # Variáveis de ambiente com as credenciais do banco (NÃO versionar)
├── .gitignore                 # Deve incluir o .env
├── logo.ico                  # Ícone da aplicação
└── 2.png                     # Imagem exibida nas telas de login/cadastro/home
```

> ⚠️ O código atual utiliza caminhos absolutos fixos (ex: `C:\Users\natan\...`) para o ícone e a imagem. Para rodar em outra máquina, é necessário ajustar esses caminhos ou torná-los relativos ao projeto.

## 🗄️ Estrutura da tabela `clientes` (banco de dados)

A aplicação espera uma tabela com, no mínimo, as seguintes colunas (na ordem em que são acessadas por índice no código):

| Índice | Campo             |
|--------|-------------------|
| 0      | id                |
| 1      | nome              |
| 2      | cpf               |
| 3      | senha (hash)      |
| 4      | email             |
| 5      | data_nascimento   |
| 6      | logradouro        |
| 7      | numero            |
| 8      | bairro            |
| 9      | cidade            |
| 10     | estado            |
| 11     | cep               |
| 12     | telefone          |

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```

2. Instale as dependências:
   ```bash
   pip install customtkinter bcrypt pillow psycopg python-dotenv
   ```

3. Crie um arquivo `.env` na raiz do projeto com as credenciais do banco:
   ```env
   DB_HOST=localhost
   DB_NAME=nome_do_banco
   DB_USER=usuario
   DB_PASSWORD=senha
   ```
   > ⚠️ Adicione `.env` ao `.gitignore` para não versionar credenciais.

4. Crie a tabela `clientes` no PostgreSQL (veja a estrutura de colunas abaixo).

5. Ajuste os caminhos das imagens (`2.png`, `logo.ico`) para o seu ambiente.

6. Execute o programa:
   ```bash
   python main.py
   ```

## 🚧 Possíveis melhorias futuras

- Tornar os caminhos de imagens/ícone relativos ao projeto (usando `os.path`)
- Adicionar validação de formato para CPF, e-mail, CEP e telefone
- Adicionar máscara de entrada (input mask) para CPF, telefone e CEP
- Implementar recuperação de senha
- Separar o código em múltiplos arquivos/módulos (telas, banco, validações)
- Evitar abrir uma conexão com o banco automaticamente ao importar `conexao_db.py` (linha `conectado = conectar_banco()`), já que cada função já abre e fecha sua própria conexão

## 📄 Licença

Projeto de estudo, sem licença definida até o momento.
