# Este é um jogo simples onde você:
# Controla um quadrado azul usando as setas do teclado (← e →)
# Deve desviar dos obstáculos vermelhos que caem
# Ganha pontos cada vez que um obstáculo passa sem atingir você
# O jogo termina se você colidir com um obstáculo
# Para jogar, você precisará:
# Ter o Python instalado

# >>>>>>>>>>>Instalar o Pygame usando o comando: pip install pygame<<<<<<<<<<<<<<<<
# Salvar o código em um arquivo chamado jogo.py
# Executar o arquivo
# Características do jogo:
# O jogador se move horizontalmente na parte inferior da tela
# Obstáculos caem do topo da tela
# A pontuação aumenta quando você consegue desviar dos obstáculos
# A velocidade é constante (você pode modificar as variáveis jogador_velocidade e obstaculo_velocidade para ajustar a dificuldade)
# Você pode personalizar o jogo alterando:
# As cores
# O tamanho da tela
# A velocidade dos elementos
# O tamanho do jogador e dos obstáculos
# Este é um exemplo básico que pode ser expandido com mais recursos como:
# Diferentes níveis de dificuldade
# Sons
# Múltiplos obstáculos
# Power-ups
# Menu principal
# Sistema de vidas


import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Desviar")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Jogador
jogador_tamanho = 50
jogador_x = LARGURA // 2 - jogador_tamanho // 2
jogador_y = ALTURA - 2 * jogador_tamanho
jogador_velocidade = 15

# Obstáculo
obstaculo_largura = 50
obstaculo_altura = 50
obstaculo_x = random.randint(0, LARGURA - obstaculo_largura)
obstaculo_y = -obstaculo_altura
obstaculo_velocidade = 16



# Pontuação
pontos = 0
fonte = pygame.font.Font(None, 36)

# Loop principal do jogo
rodando = True
clock = pygame.time.Clock()

while rodando:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= jogador_velocidade
    if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - jogador_tamanho:
        jogador_x += jogador_velocidade

    # Movimentação do obstáculo
    obstaculo_y += obstaculo_velocidade
    if obstaculo_y > ALTURA:
        obstaculo_y = -obstaculo_altura
        obstaculo_x = random.randint(0, LARGURA - obstaculo_largura)
        pontos += 1

    # Colisão
    jogador_rect = pygame.Rect(jogador_x, jogador_y, jogador_tamanho, jogador_tamanho)
    obstaculo_rect = pygame.Rect(obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura)
    
    if jogador_rect.colliderect(obstaculo_rect):
        print(f"Game Over! Pontuação: {pontos}")
        rodando = False

    # Desenho
    TELA.fill((0, 0, 0))  # Fundo preto
    pygame.draw.rect(TELA, AZUL, jogador_rect)  # Jogador
    pygame.draw.rect(TELA, VERMELHO, obstaculo_rect)  # Obstáculo
    
    # Mostrar pontuação
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    TELA.blit(texto_pontos, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 