class Cliente:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
     #ao inves de exibir o código da memória, eixbe o texto abaixo   
    def __str__(self):
        return f"Cliente(nome={self.nome}, email={self.email}, idade={self.idade})"