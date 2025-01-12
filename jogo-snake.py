# Jogo da Cobrinha

# >>>>>>>>>Instalar o Pygame usando o comando: pip install pygame no terminal<<<<<<<<<<<<<<<<

# Desenvolvido por: Luan Moraes
# A cada 50 pontos, o nível aumenta
# Cada nível adiciona 2 novos obstáculos
# O nível atual é mostrado na tela
# >>> Obstáculos:
# Blocos cinzas que não podem ser atravessados
# Colidir com um obstáculo causa game over
# Power-up azul permite atravessar obstáculos
# Power-up vermelho alimenta a cobra
# Power-up amarelo aumenta a velocidade da cobra
# Power-up roxo  aumenta a pontuação da cobra


import pygame
import random
import time

# Inicialização
pygame.init()

# Configurações
LARGURA = 800
ALTURA = 600
TAMANHO_BLOCO = 25
FPS = 7

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
ROXO = (128, 0, 128)
CINZA = (128, 128, 128)

# Configuração da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake Game')
relogio = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.tamanho = 2
        self.posicoes = [(LARGURA//2, ALTURA//2)]
        self.direcao = "DIREITA"
        self.cor = VERDE
        self.pontos = 0
        self.velocidade_bonus = 0
        self.atravessa_parede = False
        
    def mover(self):
        x, y = self.posicoes[0]
        
        if self.direcao == "CIMA":
            y -= TAMANHO_BLOCO
        elif self.direcao == "BAIXO":
            y += TAMANHO_BLOCO
        elif self.direcao == "ESQUERDA":
            x -= TAMANHO_BLOCO
        elif self.direcao == "DIREITA":
            x += TAMANHO_BLOCO
            
        # Verificar colisão com parede
        if self.atravessa_parede:
            if x >= LARGURA:
                x = 0
            elif x < 0:
                x = LARGURA - TAMANHO_BLOCO
            if y >= ALTURA:
                y = 0
            elif y < 0:
                y = ALTURA - TAMANHO_BLOCO
        else:
            if x >= LARGURA or x < 0 or y >= ALTURA or y < 0:
                return False
            
        # Verificar colisão com próprio corpo
        if (x, y) in self.posicoes[1:]:
            return False
            
        self.posicoes.insert(0, (x, y))
        if len(self.posicoes) > self.tamanho:
            self.posicoes.pop()
            
        return True
        
    def desenhar(self):
        for i, (x, y) in enumerate(self.posicoes):
            if i == 0:  # Cabeça
                pygame.draw.rect(tela, self.cor, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))
                # Olhos
                olho_tam = 4
                if self.direcao in ["ESQUERDA", "DIREITA"]:
                    pygame.draw.circle(tela, PRETO, (x + 5, y + 5), olho_tam)
                    pygame.draw.circle(tela, PRETO, (x + 5, y + 15), olho_tam)
                else:
                    pygame.draw.circle(tela, PRETO, (x + 5, y + 5), olho_tam)
                    pygame.draw.circle(tela, PRETO, (x + 15, y + 5), olho_tam)
            else:  # Corpo
                pygame.draw.rect(tela, self.cor, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))

class Comida:
    def __init__(self, tipo="normal"):
        self.tipo = tipo
        self.posicao = self.gerar_posicao()
        self.tempo_vida = 150  # Frames até desaparecer (apenas para especiais)
        
    def gerar_posicao(self):
        x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
        y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
        return (x, y)
        
    def desenhar(self):
        x, y = self.posicao
        if self.tipo == "normal":
            pygame.draw.rect(tela, VERMELHO, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))
        elif self.tipo == "velocidade":
            pygame.draw.rect(tela, AMARELO, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))
        elif self.tipo == "atravessar":
            pygame.draw.rect(tela, AZUL, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))
        elif self.tipo == "bonus":
            pygame.draw.rect(tela, ROXO, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))

class Obstaculo:
    def __init__(self):
        self.posicao = self.gerar_posicao()
        
    def gerar_posicao(self):
        x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
        y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
        return (x, y)
        
    def desenhar(self):
        pygame.draw.rect(tela, CINZA, 
                        (self.posicao[0], self.posicao[1], 
                         TAMANHO_BLOCO, TAMANHO_BLOCO))

def mostrar_pontuacao(pontos):
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(f'Pontos: {pontos}', True, BRANCO)
    tela.blit(texto, (10, 10))

def mostrar_game_over(pontos):
    fonte = pygame.font.Font(None, 72)
    texto_game_over = fonte.render('Game Over!', True, VERMELHO)
    texto_pontos = fonte.render(f'Pontos: {pontos}', True, BRANCO)
    texto_reiniciar = fonte.render('Pressione R para reiniciar', True, BRANCO)
    
    tela.blit(texto_game_over, (LARGURA//2 - 150, ALTURA//2 - 100))
    tela.blit(texto_pontos, (LARGURA//2 - 100, ALTURA//2))
    tela.blit(texto_reiniciar, (LARGURA//2 - 200, ALTURA//2 + 100))

def jogo():
    cobra = Snake()
    comida = Comida()
    comida_especial = None
    obstaculos = []  # Lista para armazenar obstáculos
    pontos_ultimo_obstaculo = 0  # Controlar quando adicionar novo obstáculo
    rodando = True
    game_over = False
    
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            elif evento.type == pygame.KEYDOWN:
                if game_over and evento.key == pygame.K_r:
                    return True
                if not game_over:
                    if evento.key == pygame.K_UP and cobra.direcao != "BAIXO":
                        cobra.direcao = "CIMA"
                    elif evento.key == pygame.K_DOWN and cobra.direcao != "CIMA":
                        cobra.direcao = "BAIXO"
                    elif evento.key == pygame.K_LEFT and cobra.direcao != "DIREITA":
                        cobra.direcao = "ESQUERDA"
                    elif evento.key == pygame.K_RIGHT and cobra.direcao != "ESQUERDA":
                        cobra.direcao = "DIREITA"
        
        if not game_over:
            # Verificar se deve adicionar novo obstáculo
            if cobra.pontos >= pontos_ultimo_obstaculo + 50:
                pontos_ultimo_obstaculo = cobra.pontos
                # Tentar posicionar obstáculo em local válido
                for _ in range(10):  # Tentar 10 vezes
                    novo_obs = Obstaculo()
                    pos = novo_obs.posicao
                    # Verificar se posição é válida
                    if (pos not in cobra.posicoes and 
                        pos != comida.posicao and
                        all(pos != obs.posicao for obs in obstaculos) and
                        abs(pos[0] - cobra.posicoes[0][0]) > TAMANHO_BLOCO * 2 and
                        abs(pos[1] - cobra.posicoes[0][1]) > TAMANHO_BLOCO * 2):
                        obstaculos.append(novo_obs)
                        break

            # Movimento da cobra
            if not cobra.mover():
                game_over = True
                
            # Verificar colisão com obstáculos
            if not cobra.atravessa_parede:  # Não verifica se estiver com power-up azul
                for obs in obstaculos:
                    if cobra.posicoes[0] == obs.posicao:
                        game_over = True
                        break

            # Verificar colisão com comida
            if cobra.posicoes[0] == comida.posicao:
                # Gerar nova comida em posição válida
                while True:
                    comida = Comida()
                    if (comida.posicao not in [obs.posicao for obs in obstaculos] and
                        comida.posicao not in cobra.posicoes):
                        break
                cobra.tamanho += 1
                cobra.pontos += 10

            # Gerenciar comida especial
            if not comida_especial and random.random() < 0.02:  # 2% de chance
                tipo = random.choice(["velocidade", "atravessar", "bonus"])
                comida_especial = Comida(tipo)
                
            if comida_especial:
                if cobra.posicoes[0] == comida_especial.posicao:
                    if comida_especial.tipo == "velocidade":
                        cobra.velocidade_bonus = 3
                    elif comida_especial.tipo == "atravessar":
                        cobra.atravessa_parede = True
                        cobra.cor = AZUL
                    elif comida_especial.tipo == "bonus":
                        cobra.pontos += 50
                    comida_especial = None
                else:
                    comida_especial.tempo_vida -= 1
                    if comida_especial.tempo_vida <= 0:
                        comida_especial = None
                        
            # Atualizar efeitos
            if cobra.velocidade_bonus > 0:
                cobra.velocidade_bonus -= 1
                if cobra.velocidade_bonus <= 0:
                    cobra.atravessa_parede = False
                    cobra.cor = VERDE
            
        # Desenho
        tela.fill(PRETO)
        # Desenhar grade para melhor visualização
        for x in range(0, LARGURA, TAMANHO_BLOCO):
            pygame.draw.line(tela, (20, 20, 20), (x, 0), (x, ALTURA))
        for y in range(0, ALTURA, TAMANHO_BLOCO):
            pygame.draw.line(tela, (20, 20, 20), (0, y), (LARGURA, y))
            
        # Desenhar obstáculos
        for obs in obstaculos:
            obs.desenhar()
            
        cobra.desenhar()
        comida.desenhar()
        if comida_especial:
            comida_especial.desenhar()
            
        # Mostrar informações
        mostrar_pontuacao(cobra.pontos)
        # Mostrar quantidade de obstáculos
        fonte = pygame.font.Font(None, 36)
        texto_obstaculos = fonte.render(f'Obstáculos: {len(obstaculos)}', True, BRANCO)
        tela.blit(texto_obstaculos, (10, 40))
        
        if game_over:
            mostrar_game_over(cobra.pontos)
            
        pygame.display.flip()
        relogio.tick(FPS + (cobra.velocidade_bonus > 0) * 2)
    
    return False

# Loop principal
while True:
    if not jogo():
        break

pygame.quit() 