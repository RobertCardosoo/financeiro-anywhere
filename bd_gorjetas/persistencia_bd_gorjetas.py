# Autor: Enoque Teixeira Barbosa
# Data de criação: 25/05/2024
# Data da última alteração: 28/05/2024
# Funções de CRUD para as entidades envolvendo o pagamento de gojetas

import mysql.connector
from contextlib import closing
from bd_gorjetas.definicoes_bd_gorjetas import DATABASE
from entidades.conta import Conta
from entidades.funcionario import Funcionario
from entidades.hospede import Hospede
from entidades.cartao import Cartao


def get_connection():
    return mysql.connector.connect(
        host=DATABASE['HOST'],
        port=DATABASE['PORT'],
        user=DATABASE['USER'],
        password=DATABASE['PASSWORD'],
        database=DATABASE['NAME']
    )

def create_tables():
    with closing(get_connection()) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    banco VARCHAR(255) NOT NULL,
                    agencia VARCHAR(255) NOT NULL,
                    numero VARCHAR(255) NOT NULL,
                    saldo DECIMAL(10,2) NOT NULL,
                    chave_pix VARCHAR(255) UNIQUE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS funcionarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    cpf VARCHAR(255) NOT NULL,
                    conta_id INT,
                    FOREIGN KEY (conta_id) REFERENCES contas(id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS hospedes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    cpf VARCHAR(255) NOT NULL,
                    conta_id INT,
                    FOREIGN KEY (conta_id) REFERENCES contas(id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cartoes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    numero VARCHAR(255) NOT NULL,
                    validade VARCHAR(255) NOT NULL,
                    cvv VARCHAR(255) NOT NULL,
                    saldo DECIMAL(10,2) NOT NULL,
                    hospede_id INT,
                    FOREIGN KEY (hospede_id) REFERENCES hospedes(id)
                )
            ''')
            conn.commit()
            
def add_conta(conta):
    with closing(get_connection()) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO contas (banco, agencia, numero, saldo, chave_pix)
                VALUES (%s, %s, %s, %s, %s)
            ''', (conta.banco, conta.agencia, conta.numero, conta.saldo, conta.chave_pix))
            conn.commit()
            return cursor.lastrowid
        
def get_conta_by_id(conta_id):
    with closing(get_connection()) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT *
                FROM contas
                WHERE id = %s
            ''', (conta_id,))
            row = cursor.fetchone()
            if row:
                conta = Conta(id=row[0], banco=row[1], agencia=row[2], numero=row[3], saldo=row[4], chave_pix=row[5])
                return conta
            return None