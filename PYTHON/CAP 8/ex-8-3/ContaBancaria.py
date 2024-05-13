class ContaBancaria:
    def __init__(self):
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
    
    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

minha_conta = ContaBancaria()

minha_conta.depositar(100)
minha_conta.exibir_saldo()

minha_conta.sacar(50)
minha_conta.exibir_saldo()
