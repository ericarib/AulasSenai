print("Bem vindo ao Banco Girabank")

saldo = float(input("digite seu saldo:R$"))

transferencia = float(input("Qual o valor da transferencia?:R$"))

#Valide se ela tem saldo suficiente para fazer uma transferencia

saldoAtual = saldo - transferencia

if saldo >= transferencia:
    print("\nValor transferido", "Seu saldo atual é de: ", saldoAtual)
else:
    print("\nsaldo insudiciente")


"""
if ternário
print("Valor transferido!" if saldo >= transferencia else "saldo insuficiente", 
    "\nSeu saldo atual é de:R$",saldoAtual)

"""