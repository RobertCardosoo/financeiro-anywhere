# Autor: Enoque Teixeira Barbosa
# Data de criação: 25/05/2024
# Data da última alteração: 28/05/2024

from entidades.conta import Conta
from entidades.cartao import Cartao
from entidades.gorjeta import Gorjeta

class Hospede:
    """
    Classe para representar um Hóspede.

    Autor: Enoque Teixeira Barbosa
    Data de criação: 25/05/2024
    Data da última alteração: 28/05/2024

    Atributos:
        id (int): ID do hóspede.
        nome (str): Nome do hóspede.
        cpf (str): CPF do hóspede.
        conta (Conta): Contas bancárias associadas ao hóspede.
        conta (Cartao): Cartões associadas ao hóspede.
    """

    def __init__(self, id, nome, cpf, contas, cartoes):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.contas = contas
        self.cartoes = cartoes

    def __str__(self):
        cartoes_str = ', '.join(str(cartao) for cartao in self.cartoes)
        return f"Hospede(id={self.id}, nome={self.nome}, cpf={self.cpf}, conta={self.conta}, cartoes=[{cartoes_str}])"

    def dar_gorjeta(self, funcionario, valor_gorjeta):
        if not isinstance(valor_gorjeta, Gorjeta):
            print("Valor de gorjeta inválido.")
            return False
        
        valor_gorjeta = valor_gorjeta.value

        if funcionario.conta and funcionario.conta.chave_pix == self.conta.chave_pix:
            if self.conta.sacar(valor_gorjeta):
                funcionario.conta.depositar(valor_gorjeta)
                print(f"Gorjeta de {valor_gorjeta} creditada na conta do funcionário {funcionario.nome}.")
                return True
            else:
                for cartao in self.cartoes:
                    if cartao.debitar(valor_gorjeta):
                        funcionario.conta.depositar(valor_gorjeta)
                        print(f"Gorjeta de {valor_gorjeta} creditada na conta do funcionário {funcionario.nome} usando cartão de crédito.")
                        return True
                print("Saldo insuficiente.")
                return False
        else:
            print("Chave PIX do funcionário não está vinculada ao cliente ou não existe.")
            return False
