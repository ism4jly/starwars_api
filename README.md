# 🌌 Star Wars Explorer API - PowerOfData Challenge

Este projeto consiste em uma API desenvolvida para o processo seletivo da **PowerOfData**. A solução permite explorar informações detalhadas sobre o universo Star Wars através de uma interface integrada à [SWAPI](https://swapi.dev/).

## 🚀 Arquitetura da Solução

A aplicação foi construída sobre a infraestrutura da **Google Cloud Platform (GCP)**, utilizando uma abordagem *Serverless* para garantir escalabilidade automática e eficiência de custos.

### Componentes Utilizados:
* **Python 3.11:** Linguagem principal utilizada para a lógica de integração e filtros.
* **Google Cloud Functions (2nd Gen):** Processamento de backend que executa o código Python em resposta a requisições HTTP.
* **Google API Gateway:** Fachada de gerenciamento da API, responsável pelo roteamento e validação de parâmetros através da especificação OpenAPI 2.0.
* **Functions Framework:** Utilizado para padronizar a entrada e saída das requisições HTTP.

---

## 🛠️ Estrutura do Projeto

starwars_api/

├── infra/

│   └── openapi.yaml      # Especificação do API Gateway (Swagger 2.0)

├── main.py               # Lógica principal da Cloud Function

├── requirements.txt      # Dependências do projeto (requests, etc.)

└── README.md             # Documentação técnica

# 📌 Como utilizar a API

A API disponibiliza um **endpoint único** que aceita parâmetros de consulta para filtrar informações.

## 🔗 URL Base

https://star-wars-gateway-2bouu72.ew.gateway.dev/explore



## ⚙️ Parâmetros Suportados

- **resource**: Define o tipo de dado  
  _(Ex: `people`, `planets`, `starships`, `films`)_  
  **Obrigatório**

- **search**: Filtro de busca por texto  
  _(Ex: `luke`, `tatooine`)_  
  **Opcional**

## 🔍 Exemplos de Chamadas

- **Buscar Personagem**

GET /explore?resource=people&search=r2


- **Listar Planetas**

GET /explore?resource=planets


- **Consultar Naves**

GET /explore?resource=starships&search=falcon


---

## ✅ Critérios de Aceite Atendidos

- **Ambiente GCP**: Implementação utilizando **Cloud Functions** e **API Gateway**
- **Linguagem**: Desenvolvimento integral em **Python**
- **Fonte de Dados**: Consumo em tempo real da **SWAPI**
- **Endpoint Único**: Disponibilização de uma rota centralizada via Gateway
- **Filtros Dinâmicos**: Suporte a parâmetros de busca específicos para cada recurso

---


## 📄 Licença

Este projeto foi desenvolvido **exclusivamente para fins de avaliação técnica** para a **PowerOfData**.

---

