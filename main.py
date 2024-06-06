from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from typing import Dict,List
import pandas as pd
import re
from integrate.models import *
from integrate.requisicoes_externas import *
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from integrate import database,schemas,models

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


@app.post("/wallets/", response_model=schemas.AnyWallet)
async def create_wallet(wallet: schemas.AnyWalletCreate, db: AsyncSession = Depends(database.get_db)):
    db_wallet = models.AnyWallet(**wallet.dict())
    db.add(db_wallet)
    await db.commit()
    await db.refresh(db_wallet)
    return db_wallet

@app.post("/cards/", response_model=schemas.AnyCard)
async def create_card(card: schemas.AnyCardCreate, db: AsyncSession = Depends(database.get_db)):
    db_card = models.AnyCard(**card.dict())
    db.add(db_card)
    await db.commit()
    await db.refresh(db_card)
    return db_card

@app.post("/transacoes/", response_model=schemas.AnyTransacoesInternas)
async def create_transacao(transacao: schemas.AnyTransacoesInternasCreate, db: AsyncSession = Depends(database.get_db)):
    db_transacao = models.AnyTransacoesInternas(**transacao.dict())
    db.add(db_transacao)
    await db.commit()
    await db.refresh(db_transacao)
    return db_transacao

@app.get("/wallets/{wallet_id}", response_model=schemas.AnyWallet)
async def read_wallet(wallet_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.AnyWallet).where(models.AnyWallet.ANY_WAL_ID == wallet_id))
    db_wallet = result.scalars().first()
    if db_wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return db_wallet

@app.get("/cards/{card_id}", response_model=schemas.AnyCard)
async def read_card(card_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.AnyCard).where(models.AnyCard.ANY_CAR_ID == card_id))
    db_card = result.scalars().first()
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return db_card

@app.get("/cards_list/{wallet_id}", response_model=List[schemas.AnyCard])
async def read_card(wallet_id:int,db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.AnyCard).where(models.AnyCard.ANY_WAL_ID == wallet_id))
    db_cards = result.scalars().all()
    if db_cards is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return [card.__dict__ for card in db_cards]

@app.get("/transacoes/{transacao_id}", response_model=schemas.AnyTransacoesInternas)
async def read_transacao(transacao_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.AnyTransacoesInternas).where(models.AnyTransacoesInternas.ANY_TRA_ID == transacao_id))
    db_transacao = result.scalars().first()
    if db_transacao is None:
        raise HTTPException(status_code=404, detail="Transacao not found")
    return db_transacao

@app.get("/transacoes_list/{card_id}", response_model=List[schemas.AnyTransacoesInternas])
async def read_transacao(card_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.AnyTransacoesInternas).where(models.AnyTransacoesInternas.ANY_CAR_ID == card_id))
    db_transacao = result.scalars().all()
    if db_transacao is None:
        raise HTTPException(status_code=404, detail="Transacao not found")
    return [transation.__dict__ for transation in db_transacao]