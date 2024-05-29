from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import pandas as pd
import re
import uvicorn
from entidades.conta import Conta
from entidades.funcionario import Funcionario
from entidades.hospede import Hospede
from entidades.cartao import Cartao
from entidades.gorjeta import Gorjeta
from bd_gorjetas.persistencia_bd_gorjetas import create_tables, add_conta, get_conta_by_id

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


@app.get('/buscar_conta_por_id/{id}')
async def buscar_conta(id: int):
    conta = get_conta_by_id(id)
    if conta:
        return conta
    else:
        raise HTTPException(status_code=404, detail="Conta não encontrada")


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
