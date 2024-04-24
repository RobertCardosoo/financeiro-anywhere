# financeiro-anywhere

WEBSERVICE VOLTADO PARA VERIFICAÇÃO DE VALIDADE DE DADOS BANCÁRIOS

ESTA API UTILIZA COMO BASE DE DADOS A RELAÇÃO DE AGÊNCIAS DISPONIBILIZADA PELO BANCO CENTRAL DO BRASIL.

RELAÇÃO: 01/2024

API DESENVOLVIDA EM FASTAPI 0.110.1

DEPENDÊNCIAS

openpyxl               3.1.2
pandas                 2.2.2
uvicorn                0.29.0


SERVIDOR : http://15.229.91.141/

ENDPOINTS DISPONÍVEIS

\verifica_agencia\{agencia}

Realiza a verificação de existência da agência informada! Se válida, o servidor irá retorno em Json as seguintes informações:

{
    "validate": xxx, -- Retorno lógico da validade da agência inserida.
    "return": xxx, -- Retorno em string da situação da requisição
    "data": [xxx] -- Retorno em Array das informações de agências que possuem o código informado.
}

Exemplo:

Requisição: http://15.229.91.141/verifica_agencia/3546

Retorno:

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

