from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import pandas as pd
import re
from integrate.bd import *
import uvicorn
from integrate.requisicoes_externas import *

app = FastAPI()
ag = pd.read_excel('integrate/agencias.xlsx')

def remover_espacos_extra(string):
            return re.sub(r'\s+', ' ', string.strip())

@app.get("/verifica_agencia/{agencia}")
async def verifica_agencia(agencia:str):
    """Verifica se a quantidade de caracteres da agência e da conta está correta."""
    if len(agencia) != 4:
        return {'validacao':False,'Retorno': "Agência deve conter 4 digitos."}
    
    
    agencias_cod = ag['COD_COMPE_AG']
    
    if int(agencia) in agencias_cod:
        # Função para remover espaços extras de uma string
        

        # Encontrar o índice da linha onde o valor ocorre na coluna "COD_COMPE_AG"
        indice_linha = ag.index[ag['COD_COMPE_AG'] == int(agencia)]

        # Obter a linha do DataFrame
        linha = ag.loc[indice_linha]
        #Criando lista de retorno de dados
        retorno_info = list()
        # Converter a linha em um dicionário
        linha_dict = linha.to_dict(orient='records')
        for i in linha_dict:
            # Remover espaços extras das strings no dicionário e adicionar na lista de retorno
            retorno_info.append({chave: remover_espacos_extra(valor) for chave, valor in i.items() if isinstance(valor, str)})
        
        
        return {"validate":True,'return':'Agência válida!','data':retorno_info}
    

    else:
        return {"validacao":False,'retorno':'Agência inválida!'}
    

@app.get('/bancos')
async def relacao_bancos():

    instituicoes = ag['NOME_INSTITUICAO']

    lista = instituicoes.to_list()
    lista_bancos = list()
    for i in lista:
        lista_bancos.append(remover_espacos_extra(str(i)))

    retorno_lista = list(set(lista_bancos))
    retorno_lista.sort()
    retorno_lista.remove('nan')

    return retorno_lista


@app.get('/verifica_cartao/{primeiros_oito_dig}')
async def verificando(primeiros_oito_dig:str):
    resposta = retorna_cartao(primeiros_oito_dig)

    return {'Bandeira':resposta['brand'],
            'Banco':resposta['bank']['name']}
    