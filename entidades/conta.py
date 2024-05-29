# Autor: Enoque Teixeira Barbosa
# Data de criação: 25/05/2024
# Data da última alteração: 28/05/2024

class Conta:
    """
    Classe para representar uma Conta Bancária.

    Autor: Enoque Teixeira Barbosa
    Data de criação: 25/05/2024
    Data da última alteração: 28/05/2024

    Atributos:
        id (int): ID da conta.
        banco (str): Nome da instituição bancária da conta.
        agencia (int): Agência da conta.
        numero (int):Número da conta.
        saldo (decimal): saldo da conta.
        chave_pix (str): chave pix da conta.
    """
    def __init__(self, id, banco, agencia, numero, saldo=0.0, chave_pix=None):
        self.id = id
        self.banco = banco
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.chave_pix = chave_pix

    def __str__(self):
        return f"Conta(banco={self.banco}, agencia={self.agencia}, numero={self.numero}, saldo={self.saldo}, chave_pix={self.chave_pix})"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
