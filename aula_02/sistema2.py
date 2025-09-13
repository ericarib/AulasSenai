# Sistema gerenciador de Nomes

nomes = ["erica"]

def excluirNome(nome):
    for nome in nomes:
        nomes.remove(nome)

def contarnome(nome):
    return len(nomes)
print(contarnome(nomes)) 


"""while True:
    print("===== Menu de opções ========")
    print("1 - Adicionar nomes")
    print("2 - Listar nomes")
    print("3 - Excluir nomes")
    print("9 - Sair do Sistema")

    opcao = input("Escolha sua opção: ")
    if opcao == "1":
        nome = input("Digite um novo nome: ")
        # append -> Adicionar itens a lista
        nomes.append(nome)
        print("\nNome adicionada com sucesso!")

    elif opcao == "2":
        if len (nomes) == 0:
            print("Não existem nomes")
        else:
            print(nomes)
    elif opcao == "3":
        if len (nomes) == 0:
            print("Não existem nomes")
        else:
            nomeexcluir = excluirNome(input("qual nome deseja excluir? "))
    elif opcao == "9":
        print("\nSistema fechado!")
        break
    else:
        print("\nTente novamente\n")"""



