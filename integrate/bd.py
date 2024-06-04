import mysql.connector
import configparser
from pathlib import Path

config = configparser.ConfigParser()


# Caminho do arquivo que você quer verificar
caminho_arquivo = Path('config.ini')

# Verificar se o arquivo existe
if not caminho_arquivo.is_file():
    print('CONFIGURAÇÃO DO BANCO DE DADOS:')
    config['CONEXAO'] = {
    'host': input('Host:'),
    'port': input('Port:'),
    'user': input('user:'),
    'pw':  input('password:')
}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    pass

def conecta_bd():
    config_bd = configparser.ConfigParser()
    config_bd.read('config.ini')
    conn = mysql.connector.connect(
        user=config_bd['CONEXAO']['user'],
        password=config_bd['CONEXAO']['pw'],
        host=config_bd['CONEXAO']['host'],
        database='ugs',
        raise_on_warnings=True)
    return conn    
def desconecta_bd(conexao):
    conexao.close()


def lista():

    conn = conecta_bd()
    curso = conn.cursor()
    curso.execute('SELECT * FROM UGS_FUNCIONARIOS')
    retorno = curso.fetchall()
    desconecta_bd(conn)

    return retorno









