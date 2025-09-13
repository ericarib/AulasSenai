from models.cliente import Cliente
from database.database import BancoFake

class cliente_controller:
    def __init__(self):
        #conexao com Banco
        self.database = BancoFake()

    def criar_cliente(self, nome, email, idade):
        #Criar objeto cliente
        novo_cliente = Cliente(nome, email, idade)

        #Convertendo para dict -> JSON
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }

        self.database.adicionar_cliente(dict_cliente)
        print("cliente cadastrado com sucesso!")

    def listar_cliente(self):
        '''
        retornar uma lista cm todos os clientes
        '''
        return self.database.listar_clientes()