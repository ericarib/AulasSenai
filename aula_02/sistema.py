# Sistema de tarefas

tarefas = []  # lista Vazia

while True:
    print("===== Menu Tarefas ========")
    print("1 - Adicionar tarefa")
    print("2 - Listar Tarefas")
    print("9 - Sair do Sistema")

    opcao = input("Escolha sua opção: ")

# Opção 1 selecionada usando input mais append para inserir o input na lista vazia
    if opcao == "1":
        tarefa = input("Digite uma nova tarefa: ")
        # append -> Adicionar itens a lista
        tarefas.append(tarefa)
        print("\nTarefa adicionada com sucesso!")

# Opção 2 selecionada usando len para contar o numero de itens na lista e for para percorrer os itens da lista
    elif opcao == "2":
        # len -> Length -> tamanho
        if len(tarefas) == 0:
            print("\nNão existem tarefas")
        else:
            for tarefa in tarefas:
                print("\nTarefas cadastradas: ", tarefa)
# Opção 3 selecionada usando break para sair do sistema e reiniciar   
    elif opcao == "9":
        print("\nSistema fechado!")
        break
    else:
        print("\nTente novamente\n")        