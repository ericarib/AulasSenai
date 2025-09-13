from models.Pessoa import Pessoa

def menu():
    print("====Menu======")
    print("1 - Criar Pessoa")
    print("2 - Listar Pessoas")
    print("3 - Limpar Lista")
    print("9 - Sair do Sistema")

def iniciarSistema():
    print("sistema Inciado!")
    pessoas = [] #Criar lista de Pessoas
    while(True):
        menu()
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            nome = input("Nome da Pessoa: ")
            email = input("Email da Pessoa: ")
            pessoa = Pessoa(nome, email) #Manifestando a entidade(classe/objeto) 
            pessoas.append(pessoa)#Adicionar a lista de pessoas 
        elif opcao =="2":
            for pessoa in pessoas:
                print(pessoa)
                print(f'Nome: {pessoa.get_nome()}, Email: {pessoa.get_email()}')
        elif opcao == "3":
            pessoas.clear
            
        else:
            break
# Lógica para inciar automaticamente
if __name__ == "__main__":
    iniciarSistema()

    