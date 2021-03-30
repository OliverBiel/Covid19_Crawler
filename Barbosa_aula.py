class Conta:
    def __init__(self, numero, nome_cliente, saldo, limite):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.saldo = saldo
        self.limite = limite

    def get_numero(self):
        return self.numero

    def get_nome_cliente(self):
        return self.nome_cliente

    def get_saldo(self):
        return self.saldo

    def get_limite(self):
        return self.limite

    def set_numero(self, novo_numero):
        self.numero = novo_numero

    def set_nome_cliente(self, novo_nome):
        self.nome_cliente = novo_nome

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def set_limite(self, novo_limite):
        self.limite = novo_limite
