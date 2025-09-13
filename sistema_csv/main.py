from controller.cliente_controller import cliente_controller

def exibir_menu ():
    print("====Menu=======")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("0 - Sair do Sistema")

def main():
   clienteController = cliente_controller()

   while True:
       exibir_menu()
       opcao = input ("Escolha uma opção: ") 

       if opcao == "1":
            nome = input("Nome da Pessoa: ")
            email = input("Email da Pessoa: ")
            idade = int(input("Qual sua idade: "))
            #Salvar no banco de dados
            clienteController.criar_cliente(nome,email,idade) 
       elif opcao =="2":
            #Listar cliente
            clientes = clienteController.listar_cliente()
            for index, cliente in enumerate(clientes, 1):
                print(f'{index}, {cliente}')        
       elif opcao == "0":
           print("saindo do sistema")
       else:
           print("opção Inválida")

if __name__ == "__main__":
    main()
