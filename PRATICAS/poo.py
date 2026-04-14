from datetime import datetime
import pytz




             
class ContaCorrente():

    @staticmethod
    def _data_hora():

        fuso_BR = pytz.timezone('America/Sao_Paulo')
        data_hora_BR = datetime.now(fuso_BR)
        return data_hora_BR.strftime('%d/%m/%Y %H:%M:%S')
       

    def __init__(self, nome, cpf, agencia, num_conta):

        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.num_conta = num_conta
        self._saldo = 0
        self.limite = None
        self.transacoes = []
        self.tratacpf()

    def tratacpf(self):
        cpf_limpo = ''

        for caracter in self.cpf:
            if caracter.isdigit():
                cpf_limpo += caracter

        self.cpf = cpf_limpo            

    def deposito(self, valor):
        self._saldo += valor
        self.transacoes.append(('Depósito', valor, ContaCorrente._data_hora()))
        print('Depósito executado com sucesso!')

    def saque(self, valor):

        if valor > self._limite_conta():
            print('Saque não realizado, motivo: saldo insuficiente.')

        else:
            self._saldo -= valor
            self.transacoes.append(('Saque', -valor, ContaCorrente._data_hora()))
            print('Saque realizado com sucesso!')
    
    def _limite_conta(self):
        self.limite = -1000
        return self.limite
    
    def consultalimite(self):
        print(f'O seu limite de crédito é de {self.limite} reais.')

    def consulta(self):
        print(f'O seu saldo atual é de {self._saldo} reais.')
    
    def consulta_transacao(self):
        print('Historico de Transações:')
        for transacao in self.transacoes:
            print(transacao)

    def transferencia(self, valor, conta_destino):
        self._saldo -= valor
        self.transacoes.append(('Transferencia', -valor, ContaCorrente._data_hora()))

        conta_destino.saldo += valor
        conta_destino.transacoes.append(('Transferencia', valor, ContaCorrente._data_hora()))

    
    def getdados(self):
        print(f'Nome: {self.nome}\nCpf: {self.cpf}\n')

