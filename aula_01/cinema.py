print("----------------------------")
print("Bem vindo ao CINEMA Gatoflix")
print("----------------------------")

idade = int(input("digite sua idade: "))

# Estrutura de decisão
if idade >= 35:
    print("Não pode entrar")
elif idade >=18:
    print("pode entrar no gatoflix!")    
else:
    print("Não pode entrar no gatoflix!")

""" 
if = se
elif = caso se
else = caso contrario

> = maior que
< = menor que
>= = maior ou igual
<= = menor ou igual
==  = igualdade
 """

# If Ternário
# print("pode entrar" if idade >= 18 else "nao pode entrar") 

# IF resumido
#  resultado = "pode entrar" if idade > 18 else "Não pode entrar"


