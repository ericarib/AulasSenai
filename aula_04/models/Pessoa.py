class Pessoa:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


    def cadastrar (self):
        print("cadastrando Pessoa")

    def sair(self):
        print("Sair do sistema")