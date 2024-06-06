from sqlalchemy import Column, Integer, String, Boolean, DECIMAL, ForeignKey, DateTime, func, VARCHAR, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class AnyWallet(Base):
    __tablename__ = 'ANY_WALLET'

    ANY_WAL_ID = Column(Integer, primary_key=True, autoincrement=True)
    ANY_WAL_USR = Column(Integer, unique=True, nullable=False)

    cards = relationship("AnyCard", back_populates="wallet")

class AnyCard(Base):
    __tablename__ = 'ANY_CARD'

    ANY_CAR_ID = Column(Integer, primary_key=True, autoincrement=True)
    ANY_CAR_TIPO = Column(VARCHAR(1), nullable=False)
    ANY_CAR_NUMERO = Column(VARCHAR(16), nullable=False)
    ANY_CAR_FLAG = Column(TEXT, nullable=False)
    ANY_CAR_NACIONALIDADE = Column(VARCHAR(1), nullable=False)
    ANY_CAR_TITULAR = Column(VARCHAR(100), nullable=False)
    ANY_CAR_CPF = Column(VARCHAR(11), nullable=False)
    ANY_CAR_ATIVO = Column(Boolean, default=True, nullable=False)
    ANY_WAL_ID = Column(Integer, ForeignKey('ANY_WALLET.ANY_WAL_ID'), nullable=False)

    wallet = relationship("AnyWallet", back_populates="cards")
    transactions = relationship("AnyTransacoesInternas", back_populates="card")

class AnyTransacoesInternas(Base):
    __tablename__ = 'ANY_TRANSACOES_INTERNAS'

    ANY_TRA_ID = Column(Integer, primary_key=True, autoincrement=True)
    ANY_TRA_VALOR = Column(DECIMAL(9, 2), nullable=False)
    ANY_TRA_TIPO = Column(VARCHAR(1), nullable=False)
    ANY_TRA_NUM_PARCELAS = Column(Integer, default=1, nullable=False)
    ANY_TRA_REGISTRO = Column(DateTime, default=func.current_timestamp(), nullable=False)
    ANY_TRA_OPERACAO = Column(VARCHAR(1), nullable=False)
    ANY_CAR_ID = Column(Integer, ForeignKey('ANY_CARD.ANY_CAR_ID'), nullable=False)

    card = relationship("AnyCard", back_populates="transactions")
