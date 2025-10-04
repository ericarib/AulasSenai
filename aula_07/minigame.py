import pygame, sys

# Iniciando jogo
pygame.init()

# Criando tela do jogo (x, y)
screen = pygame.display.set_mode((400, 300))

# posição inicial da bolinha 
x = 200
y = 150

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
    

    #Pintar fundo do jogo, RGB (0, 0 ,0 )
    screen.fill((0, 0, 0))

    # Desenhar um circulo vermelho, RGB (255, 0, 0)
    # Cor RGB, Posição X e Y com raio 20
    pygame.draw.circle(screen,(255,0,0), (x, y), 20)

    pygame.display.flip()
