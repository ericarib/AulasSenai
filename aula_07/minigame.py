import pygame, sys
import random

# Iniciando jogo
pygame.init()

# Criando tela do jogo (x, y)
screen = pygame.display.set_mode((400, 300))

# carregar imagem 
player_img = pygame.image.load("personagem.png")

food_img = pygame.image.load("comida.png")
food_img = pygame.transform.scale(food_img, (20, 20))

# posição inicial da bolinha 
x = 200
y = 150
tamanho = 40
velocidade = 5

    # posição aleatoria da comida
food_x = random.randint(20, 380)  #meu limite é 400
food_y = random.randint(20, 280) # meu limite é 300


while True:
    # Veriicar todos os eventos
    for event in pygame.event.get():
        # O jogador clicou no X da guia e saiu do jogo
        if event.type == pygame.QUIT:
            sys.exit()

    # Pegar as teclas do jogador
    keys = pygame.key.get_pressed()

    # Andar para a esquerda
    if keys[pygame.K_LEFT]:
        x -= 0.2
    # Andar para a direira
    if keys[pygame.K_RIGHT]:
        x += 0.2
    # Andar para cima
    if keys[pygame.K_UP]:
        y -= 0.2
    # Andar para baixo
    if keys[pygame.K_DOWN]:
        y += 0.2

    # Dr X for maior que 0, colocamos o tamanho da bolinha
    if x < 0:
        x = 0
    # Dr X for maior que 400, colocamos menos o ramanho da bolinha
    if x > 400 - tamanho:
        x = 400 - tamanho

    if y < 0:
        y = 0
    if y > 300 - tamanho:
        y = 300 - tamanho

    centro_player_x = x + tamanho / 2
    centro_player_y = y + tamanho / 2

    centro_food_x = food_x + 10
    centro_food_y = food_y + 10

    diferenca_x = centro_player_x - centro_food_x
    diferenca_y = centro_player_y - centro_food_y

    quadrado_x = diferenca_x ** 2
    quadrado_y = diferenca_y ** 2

    soma_dos_quadrados = quadrado_x + quadrado_y

    # raiz da sima dos quadrados
    distancia = soma_dos_quadrados ** 0.5

    if distancia < (tamanho /2 +10): # se encostar (o raio 10 é o tamanho da bolinha amarela)
        tamanho += 5 # aumenta a bolinha vermelha


        food_x = random.randint (20, 380)
        food_y = random.randint (20, 280)

    # Redimencionar a imagem do jogador 
    player_scaled = pygame.transform.scale(player_img, (tamanho, tamanho))

    #Pintar fundo do jogo, RGB (0, 0 ,0 )
    screen.fill((0, 0, 0))

    screen.blit(food_img, (food_x, food_y))
    screen.blit(player_scaled, (x, y))

    pygame.display.flip()
