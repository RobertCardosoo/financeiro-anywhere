from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


@app.get("/verify/{agencia}/{conta}")
async def verificar_tamanho_agencia_e_conta(agencia:str, conta:str):
    """Verifica se a quantidade de caracteres da agência e da conta está correta."""
    if len(agencia) != 5:
        return False, "A agência deve ter 5 caracteres."
    if len(conta) != 8:
        return False, "A conta deve ter 8 caracteres."
    return {'Validacao':True,'Retorno': "Agência e conta têm o número correto de caracteres."}

