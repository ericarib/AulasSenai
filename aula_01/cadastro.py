# Solicite o nome email e senha do usuário 
#  logo em seguida realize um print com suas infos

nome = str (input("Digite seu nome: "))
email = str(input("Digite seu email "))
senha = int(input("digite uma senha de 4 digitos "))

# verificador de itens inputados
if nome.strip() == "":
      print("O nome não foi preenchido")

print("\nsegue abaixo seus dados cadastrados"
      "\n"  
      "\nseu nome é: ", nome, 
      "\nobrigado por fornecer seu email: ", email, 
      "\nSua senha é: ", senha)

# Criar um sistema de cadastro de notas

print("\nSISTEMA INTEGRADO DE NOTAS")

Nota1 = float (input('Digite a primeira nota: '))
Nota2 = float (input('Digite a segunda nota: '))
Nota3 = float (input('Digite a terceira nota: '))
Nota4 = float (input('Digite a quarta nota: '))

resultado = (Nota1 + Nota2 + Nota3 + Nota4) / 4

#  Status = "Reprovado" if resultado < 7 else "Aprovado"

print('\nA média deste aluno é de ', resultado)