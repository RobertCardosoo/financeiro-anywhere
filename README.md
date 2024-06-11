## Anywhere Financeiro - API de Validação de Dados Bancários

**Introdução**

Este Readme documenta a API de Validação de Dados Bancários, um serviço web desenvolvido para auxiliar na verificação da existência e validade de agências bancárias no Brasil. A API utiliza como base de dados a relação de agências disponibilizada pelo Banco Central do Brasil, atualizada em janeiro de 2024.

## Funcionalidades

A principal funcionalidade da API é verificar a existência e validade de agências bancárias. Através do endpoint `verifica_agencia/{agencia}`, a API consulta a base de dados e retorna um JSON com informações sobre a agência, caso seja válida.

## Servidor

A API está disponível no servidor `http://15.229.91.141/`.

## Endpoints

### `/verifica_agencia/{agencia}` (GET)

**Funcionalidade:** Verifica a existência da agência informada (`agencia`).

**Método:** GET

**Parâmetros:** `agencia` (identificador da agência)

**Retorno:** JSON com informações sobre a agência:

* `validate`: Booleano indicando se a agência é válida.
* `return`: Mensagem informativa sobre a situação da requisição.
* `data`: Array contendo informações detalhadas da agência (se válida):
    * `CNPJ`: CNPJ da instituição bancária.
    * `NOME_INSTITUICAO`: Nome completo da instituição bancária.
    * `SEGMENTO`: Segmento de atuação da instituição bancária.
    * `NOME_AGENCIA`: Nome da agência.
    * `ENDERECO`: Endereço completo da agência.
    * `NUMERO`: Número da agência.
    * `COMPLEMENTO`: Complemento do endereço da agência.
    * `BAIRRO`: Bairro da agência.
    * `CEP`: CEP da agência.
    * `MUNICIPIO`: Município da agência.
    * `UF`: Unidade Federativa (estado) da agência.

**Exemplo de requisição:**

GET http://15.229.91.141/verifica_agencia/3546

**Exemplo de resposta:**

````json
{
  "validate": true,
  "return": "Agência válida!",
  "data": [
    {
      "CNPJ": "00.000.000",
      "NOME_INSTITUICAO": "BANCO DO BRASIL S.A.",
      "SEGMENTO": "Banco do Brasil - Banco Múltiplo",
      "NOME_AGENCIA": "FRANCISCO PORTO",
      "ENDERECO": "AV FRANCISCO PORTO, 566",
      "NUMERO": "",
      "COMPLEMENTO": "",
      "BAIRRO": "S FILHO",
      "CEP": "49020-570",
      "MUNICIPIO": "ARACAJU",
      "UF": "SE"
    },
    {
      "CNPJ": "00.360.305",
      "NOME_INSTITUICAO": "CAIXA ECONOMICA FEDERAL",
      "SEGMENTO": "Caixa Econômica Federal",
      "NOME_AGENCIA": "SANTA MARIA DA VITORIA, BA",
      "ENDERECO": "PRACA ARGEMIRO FILARDES, NUM S/N",
      "NUMERO": "",
      "COMPLEMENTO": "",
      "BAIRRO": "CENTRO",
      "CEP": "47640-000",
      "MUNICIPIO": "SANTA MARIA DA VITORIA",
      "UF": "BA"
    }
  ]
}
````

### `/bancos` (GET)

**Funcionalidade:** Recupera uma lista de instituições bancárias disponíveis na base de dados.


**Método:** GET

**Retorno:** Uma lista com todas as instituições bancárias disponíveis na base de dados

**Exemplo de requisição:**

GET http://15.229.91.141/bancos

**Exemplo de resposta:**

````json
[
    "BANCO C6 S.A.",
    "BANCO CAIXA GERAL - BRASIL S.A.",
    "BANCO CARGILL S.A.",
    "BANCO CATERPILLAR S.A.",
    "BANCO CEDULA S.A.",
    "BANCO CIFRA S.A.",
    "BANCO CITIBANK S.A.",
]
````

### `/wallets` (POST)

**Funcionalidade:** Cria uma nova carteira para armazenar dados de cartões e realizar transações. Requer autenticação e envio de dados no formato JSON no corpo da requisição.

**Método:** POST

**Retorno:** Um dicionário JSON contendo as informações da carteira:

**Exemplo de requisição:**

POST http://15.229.91.141/wallets/{id}

## Tecnologia

A API foi desenvolvida utilizando a biblioteca FastAPI para Python, versão 0.110.1. As dependências adicionais incluem:

* openpyxl 3.1.2
* pandas 2.2.2
* uvicorn 0.29.0