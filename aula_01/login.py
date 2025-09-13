print ("Sistema Administrativo")

usuario = input ("Digite o usuário: " )
senha = input ("Digite sua senha: ")

if usuario == "admin":
    if senha == "12345":
        print("\nlogin bem sucedido!")
    else:
        print("Senha incorreta!")
else:
    print("Usuario inválido!") 

     