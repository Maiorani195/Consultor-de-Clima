
# 🌤️ Consultor de Clima CLI

Uma aplicação de interface de linha de comando (CLI) desenvolvida em Python para consultar dados meteorológicos em tempo real de qualquer cidade do mundo. 

Este projeto consome a API RESTful do **OpenWeatherMap** e foi estruturado com foco em boas práticas de desenvolvimento, incluindo modularização de código e proteção de credenciais.

## 🚀 Funcionalidades

* **Consulta em Tempo Real:** Busca dados atualizados de temperatura, sensação térmica, umidade e vento.
* **Interface ** Retorno visual no terminal utilizando emojis baseados nas condições climáticas (sol, chuva, neve, etc.).
* **Tratamento de Erros:** Validação de status HTTP (cidade não encontrada, chave inválida) e proteção contra quedas de conexão.
* **Segurança:** Utilização de variáveis de ambiente (`.env`) para ocultar a API Key.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **requests** (Integração com a API)
* **python-dotenv** (Gerenciamento de variáveis de ambiente)

## 📁 Estrutura do Projeto

A arquitetura foi modularizada para separar as regras de negócio da interface com o usuário:

```text
├── main.py           # Interface do usuário e menu interativo
├── clima_api.py      # Lógica de requisição e formatação de dados da API
├── .env.example      # Exemplo de configuração das variáveis de ambiente
├── .gitignore        # Ignora arquivos sensíveis (.env) e pastas do sistema
└── README.md         # Documentação do projeto
