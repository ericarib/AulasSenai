class ContaBancaria:
    
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
       if valor <=  self.saldo:
          self.saldo =  self.saldo - valor
          return True
       else:
           return False
       
    def get_saldo(self):
        return self.saldo
    
ContaGeraldo = ContaBancaria(10000000000000000000000000000000000000000000000)
ContaGeraldo.sacar(50)
ContaGeraldo.depositar(50000)
print(ContaGeraldo.get_saldo())