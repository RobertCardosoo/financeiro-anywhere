# Autor: Enoque Teixeira Barbosa
# Data de criação: 25/05/2024
# Data da última alteração: 28/05/2024

from entidades.conta import Conta

class Funcionario:
    """
    Classe para representar um Funcionário.

    Autor: Enoque Teixeira Barbosa
    Data de criação: 25/05/2024
    Data da última alteração: 28/05/2024

    Atributos:
        id (int): ID do funcionário.
        nome (str): Nome do funcionário.
        cpf (str): CPF do funcionário.
        contas (Conta): Contas bancárias associadas ao funcionário.
    """
    
    def __init__(self, id, nome, cpf, contas):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.contas = contas

    def __str__(self):
        return f"Funcionario(id={self.id}, nome={self.nome}, cpf={self.cpf}, conta={self.conta})"
