from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AnyWalletBase(BaseModel):
    ANY_WAL_USR: int

class AnyWalletCreate(AnyWalletBase):
    pass

class AnyWallet(AnyWalletBase):
    ANY_WAL_ID: int

    class Config:
        orm_mode = True

class AnyCardBase(BaseModel):
    ANY_CAR_TIPO: str
    ANY_CAR_NUMERO: str
    ANY_CAR_FLAG: str
    ANY_CAR_NACIONALIDADE: str
    ANY_CAR_TITULAR: str
    ANY_CAR_CPF: str
    ANY_CAR_ATIVO: bool
    ANY_WAL_ID: int

class AnyCardCreate(AnyCardBase):
    pass

class AnyCard(AnyCardBase):
    ANY_CAR_ID: int

    class Config:
        orm_mode = True

class AnyTransacoesInternasBase(BaseModel):
    ANY_TRA_VALOR: float
    ANY_TRA_TIPO: str
    ANY_TRA_NUM_PARCELAS: int
    ANY_TRA_REGISTRO: datetime
    ANY_TRA_OPERACAO: str
    ANY_CAR_ID: int

class AnyTransacoesInternasCreate(AnyTransacoesInternasBase):
    pass

class AnyTransacoesInternas(AnyTransacoesInternasBase):
    ANY_TRA_ID: int

    class Config:
        orm_mode = True
