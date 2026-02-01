# 🌌 Star Wars Explorer API - PowerOfData Challenge

Este projeto consiste em uma API desenvolvida para o processo seletivo da **PowerOfData**. A solução permite explorar informações detalhadas sobre o universo Star Wars através de uma interface integrada à [SWAPI](https://swapi.dev/).

## 🚀 Diferenciais Técnicos (Valor Agregado)

Além dos requisitos básicos, esta solução implementa funcionalidades avançadas de engenharia de dados:

* **Data Hydration(Dados Correlacionados)**: Através do parâmetro expand=true no recurso de filmes, a API resolve automaticamente links de personagens para nomes reais, enriquecendo o payload.

* **Smart Sorting**: Motor de ordenação dinâmica que diferencia tipos de dados (numéricos vs. texto), garantindo precisão em campos como diameter ou population.

* **Segurança**: Autenticação via Header x-api-key com gestão de segredos por variáveis de ambiente (.env), seguindo os princípios do Twelve-Factor App.

* **Qualidade de Software**: Implementação de Testes Unitários Automatizados com pytest e Mocks para garantir a integridade da lógica sem dependência da rede.

## 🚀 Arquitetura da Solução

A aplicação foi construída sobre a infraestrutura da **Google Cloud Platform (GCP)**, utilizando uma abordagem *Serverless* para garantir escalabilidade automática e eficiência de custos.

## Desenho da Arquitetura Técnica

    Cliente->>Gateway: Request com x-api-key
    Gateway->>CF: Valida contrato e encaminha
    CF->>CF: Valida Chave (os.getenv)
    CF->>SWAPI: Fetch Data (Requests)
    Note over CF: Se expand=true: Realiza Hydration
    CF->>CF: Ordenação Numérica/Texto
    CF-->>Cliente: JSON Estruturado (200 OK)

### Componentes Utilizados:
* **Python 3.14 & Flask**: Lógica principal e gerenciamento de requisições.
* **Google Cloud Functions**: Processamento backend escalável.
* **Google API Gateway**: Gerenciamento, roteamento e segurança via OpenAPI 2.0.
* **python-dotenv**: Gestão segura de configurações e chaves.


---

## 🛠️ Estrutura do Projeto

starwars_api/

├── infra/

│   └── openapi.yaml      # Especificação do API Gateway

├── main.py               # Lógica principal e StarWarsService

├── requirements.txt      # Dependências do projeto (requests, etc.)

├── .env                  # Variáveis de ambiente (não versionado)

├── .gitignore            # Proteção de arquivos sensíveis

└── README.md             # Documentação técnica

# 📌 Como utilizar a API



## 🔗 URL Base

https://star-wars-gateway-2bouu72.ew.gateway.dev/explore



## ⚙️ Parâmetros Suportados

- **resource**: Define o tipo de dado  
  _(Ex: `people`, `planets`, `starships`, `films`)_  
  **Obrigatório**

- **search**: Filtro de busca por texto  
  _(Ex: `luke`, `tatooine`)_  
 
- **sort_by**: Campo para ordenação
  _(Ex: `diameter`, `name`)_ 

- **expand**: Resolve nomes (apenas para filmes)
  _(Ex: `true`)_

## 🔍 Exemplos de Chamadas

- **Buscar Personagem**

GET /explore?resource=people&search=r2


- **Listar Planetas**

GET /explore?resource=planets


- **Consultar Naves**

GET /explore?resource=starships&search=falcon

## Exemplos de Chamadas Avançadas

**Listar Planetas Ordenados por Diâmetro (Numérico)**: GET /explore?resource=planets&sort_by=diameter

**Consultar Filmes com Nomes de Personagens**: GET /explore?resource=films&expand=true


---

## Autenticação e Segurança
A API é protegida. Toda requisição deve conter o cabeçalho:

* **Header**: x-api-key

* **Valor**: Definido via variável de ambiente API_KEY.

---
## Qualidade e Testes
Para garantir que as novas funcionalidades (ordenação e expansão) não quebrem, execute os testes unitários:

* Instale as dependências: pip install -r requirements.txt

* Crie um arquivo .env com sua API_KEY.

* Execute: pytest test_main.py
---

## 📄 Licença

Este projeto foi desenvolvido **exclusivamente para fins de avaliação técnica** para a **PowerOfData**.

---

