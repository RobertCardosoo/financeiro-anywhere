# Autor: Enoque Teixeira Barbosa
# Data de criação: 25/05/2024
# Data da última alteração: 28/05/2024

class Cartao:
    """
    Classe para representar um funcionário.
    
    Autor: Enoque Teixeira Barbosa
    Data de criação: 25/05/2024
    Data da última alteração: 28/05/2024

    Atributos:
        id (int): ID do cartão.
        numero (int): Número do cartão.
        cvv (int): Código de segurança do cartão.
        saldo (decimal): Saldo do cartão.
    """

    def __init__(self, id, numero, validade, cvv, saldo=0.0):
        self.id = id
        self.numero = numero
        self.validade = validade
        self.cvv = cvv
        self.saldo = saldo

    def __str__(self):
        return f"Cartao(id={self.id}, numero={self.numero}, validade={self.validade}, cvv={self.cvv}, saldo={self.saldo})"

    def debitar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
