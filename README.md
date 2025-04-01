# API Operadoras - FastAPI + Vue.js

Este projeto é uma aplicação web desenvolvida com **FastAPI** no backend e **Vue.js** no frontend. A API realiza buscas de operadoras de planos de saúde a partir de um arquivo CSV, e a interface permite consultas interativas com a API.

## Tecnologias Utilizadas

- **Backend:**
  - FastAPI
  - Uvicorn
  - Pandas

- **Frontend:**
  - Vue.js

## Funcionalidades

- **Backend:** Um servidor FastAPI que expõe uma rota para buscar operadoras de planos de saúde com base em consultas textuais.
- **Frontend:** Uma interface interativa construída com Vue.js que permite enviar consultas para o servidor e exibir os resultados de forma dinâmica.

## 📁 Estrutura do Projeto

- **`data/`**: Contém o arquivo `.csv` com os dados das operadoras.
- **`backend/`**: Contém o código do backend, incluindo o arquivo `main.py`.
- **`frontend/`**: Contém os arquivos do frontend, incluindo os componentes Vue.js.
- **`backend/requirements.txt`**: Lista de dependências do backend com versões fixas.

## ▶️ Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/rianmp12/api-test.git
cd api-test
```

### 2. Configurar o Backend
#### 2.1 Criar um Ambiente Virtual (opcional, mas recomendado)

```
python -m venv venv
source venv/bin/activate   # No Linux/macOS
venv\Scripts\activate      # No Windows
```

#### 2.2 Instalar as depedências

```bash
pip install -r backend/requirements.txt
```
As versões das bibliotecas estão fixadas no `requeriments.txt` para evitar problemas com atualiazações futuras.

#### 2.3 Executar o Servidor FastAPI

Navegue até a pasta `backend` onde está o arquivo `main.py` e execute o comando:

```
python main.py
```
O servidor estará rodando em `http://localhost:8000`.

### 3. Configurar o Frontend
#### 3.1 Navegar até a pasta frontend

```
cd frontend
```

#### 3.2 Instalar as Dependências do Frontend e rodar o Servidor de Desenvolvimento

```
npm install
npm run serve
```
A aplicação frontend estará acessível em `http://localhost:8080`.

## 🔧 Importar Coleção do Postman

Para importar a coleção do Postman, siga os passos abaixo:

1. Abra o Postman.
2. Clique em "Import" no canto superior esquerdo.
3. Selecione "File" e escolha o arquivo `api-operadoras.postman_collection.json` localizado na pasta `postman/` do projeto.
4. Clique em "Import" para adicionar a coleção à sua área de trabalho do Postman.

## ✅ Requisitos Atendidos

- **Criação da API**: Desenvolvido um servidor FastAPI com uma rota para busca textual nas operadoras a partir do CSV.
- **Interface Vue.js**: Implementada uma interface web que interage com a API para realizar as buscas.
- **Coleção Postman**: Criada uma coleção no Postman para testar as rotas da API.
