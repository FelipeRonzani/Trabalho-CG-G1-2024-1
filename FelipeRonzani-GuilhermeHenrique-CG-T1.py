import pygame
from pygame.locals import *

# Constantes globais
largura_tela = 1280
altura_tela = 720
largura_jogador = 20
altura_jogador = 100
tamanho_bola = 20
velocidade_jogador = 10
velocidade_bola_x = 5
velocidade_bola_y = 5
pontos_jogador_esquerdo = 0
pontos_jogador_direito = 0

# Posições Iniciais
posicao_jogador_esquerdo = [50, altura_tela // 2 - altura_jogador // 2]
posicao_jogador_direito = [largura_tela - 50 - largura_jogador, altura_tela // 2 - altura_jogador // 2]
posicao_bola = [largura_tela // 2, altura_tela // 2]
direcao_bola = [1, 1]  # Posição da bola inicial
posicao_goleira_esquerda = [0, altura_tela // 2 - 150]
posicao_goleira_direita = [largura_tela - 25, altura_tela // 2 - 150]

# Função para desenhar um retângulo
def desenha_retangulo(surface, x, y, largura, altura, cor):
    pygame.draw.rect(surface, cor, (x, y, largura, altura))

# Função para desenhar os jogadores
def desenha_jogadores(surface):
    desenha_retangulo(surface, posicao_jogador_esquerdo[0], posicao_jogador_esquerdo[1], largura_jogador, altura_jogador, (255, 255, 255))
    desenha_retangulo(surface, posicao_jogador_direito[0], posicao_jogador_direito[1], largura_jogador, altura_jogador, (255, 255, 255))

# Função para desenhar as goleiras
def desenha_goleiras(surface):
    desenha_retangulo(surface, posicao_goleira_esquerda[0], posicao_goleira_esquerda[1], 25, 300, (255, 255, 255))
    desenha_retangulo(surface, posicao_goleira_direita[0], posicao_goleira_direita[1], 25, 300, (255, 255, 255))

# Desenha um círculo no centro do campo
def desenha_circulo_centro(surface, centro, raio, cor, largura_linha):
    pygame.draw.circle(surface, cor, centro, raio, largura_linha)

# Desenha linhas finas ao redor da tela
def desenha_linhas_bordas(surface, largura, altura, cor):
    pygame.draw.rect(surface, cor, (0, 0, largura, 10))  # Linha superior
    pygame.draw.rect(surface, cor, (0, 0, 10, altura))  # Linha esquerda
    pygame.draw.rect(surface, cor, (largura - 10, 0, 10, altura))  # Linha direita
    pygame.draw.rect(surface, cor, (0, altura - 10, largura, 10))  # Linha inferior

# Desenha um retângulo
def desenha_retangulo_goleira(surface, cor, rect):
    pygame.draw.rect(surface, cor, rect, 8)

# Desenha uma área na frente da goleira
def desenha_area_goleira(surface, cor, rect):
    desenha_retangulo_goleira(surface, cor, rect)
    # Calcula o raio do semicírculo e depois divide pela metade
    raio = rect.height // 4
    # Lado esquerdo
    if rect.left == 0:
        pygame.draw.arc(surface, cor, (rect.right - raio, rect.centery - raio, raio * 2, raio * 2), -3.141592653589793 / 2, 3.141592653589793 / 2, 8)
    # Lado direito
    else:
        pygame.draw.arc(surface, cor, (rect.left - raio, rect.centery - raio, raio * 2, raio * 2), 3.141592653589793 / 2, 3 * 3.141592653589793 / 2, 8)

# Função para desenhar o placar na tela
def desenha_placar(surface):
    fonte = pygame.font.SysFont(None, 50)
    placar_esquerdo = fonte.render(str(pontos_jogador_esquerdo), True, (255, 255, 255))
    placar_direito = fonte.render(str(pontos_jogador_direito), True, (255, 255, 255))
    surface.blit(placar_esquerdo, (largura_tela // 4, 50))
    surface.blit(placar_direito, (3 * largura_tela // 4, 50))

# Função para desenhar a bola
def desenha_bola(surface):
    pygame.draw.circle(surface, (255, 165, 0), (posicao_bola[0], posicao_bola[1]), tamanho_bola//2)

# Função para atualizar a posição da bola
def atualiza_bola():
    global posicao_bola, direcao_bola, pontos_jogador_esquerdo, pontos_jogador_direito

    # Atualiza a posição da bola
    posicao_bola[0] += direcao_bola[0] * velocidade_bola_x
    posicao_bola[1] += direcao_bola[1] * velocidade_bola_y

    # Colisão da bola com o topo e o fundo da tela
    if posicao_bola[1] <= 0 or posicao_bola[1] >= altura_tela:
        direcao_bola[1] *= -1 # Faz com que a bola vá na direção contrária

    # Colisão da bola com os lados esquerdo e direito da tela
    if posicao_bola[0] - tamanho_bola / 2 <= 0 or posicao_bola[0] + tamanho_bola / 2 >= largura_tela:
        direcao_bola[0] *= -1 # Faz com que a bola vá na direção contrária

    # Colisão da bola com os jogadores
    if posicao_bola[0] < posicao_jogador_esquerdo[0] + largura_jogador:
        # Colisão da bola com o jogador esquerdo (quando a bola está atrás)
        if (posicao_bola[0] + tamanho_bola / 2 <= posicao_jogador_esquerdo[0] + largura_jogador and
            posicao_jogador_esquerdo[1] <= posicao_bola[1] <= posicao_jogador_esquerdo[1] + altura_jogador and
            direcao_bola[0] < 0 and
            posicao_bola[0] > posicao_jogador_esquerdo[0] + largura_jogador / 2):
            direcao_bola[0] *= -1 # Faz com que a bola vá na direção contrária
    else:
        # Colisão da bola com o jogador esquerdo (quando a bola está à frente)
        if (posicao_bola[0] - tamanho_bola / 2 <= posicao_jogador_esquerdo[0] + largura_jogador and
            posicao_jogador_esquerdo[1] <= posicao_bola[1] <= posicao_jogador_esquerdo[1] + altura_jogador and
            direcao_bola[0] < 0 and
            posicao_bola[0] > posicao_jogador_esquerdo[0] + largura_jogador / 2):
            direcao_bola[0] *= -1 # Faz com que a bola vá na direção contrária

    # Checa se a bola está atrás do jogador direito
    if posicao_bola[0] > posicao_jogador_direito[0] + largura_jogador:
        # Colisão da bola com o jogador direito (quando a bola está atrás)
        if (posicao_bola[0] - tamanho_bola / 2 <= posicao_jogador_direito[0] + largura_jogador and
            posicao_jogador_direito[1] <= posicao_bola[1] <= posicao_jogador_direito[1] + altura_jogador and
            direcao_bola[0] < 0 and posicao_bola[0] > posicao_jogador_direito[0] + largura_jogador / 2):
            direcao_bola[0] *= -1 # Faz com que a bola vá na direção contrária
    else:
        # Colisão da bola com o jogador direito (quando a bola está à frente)
        if (posicao_bola[0] + tamanho_bola / 2 >= posicao_jogador_direito[0] + largura_jogador and
            posicao_jogador_direito[1] <= posicao_bola[1] <= posicao_jogador_direito[1] + altura_jogador and
            direcao_bola[0] > 0 and posicao_bola[0] > posicao_jogador_direito[0] + largura_jogador / 2):
            direcao_bola[0] *= -1 # Faz com que a bola vá na direção contrária
            
    # Colisão da bola com as goleiras
    if (posicao_bola[0] - tamanho_bola / 2 <= posicao_goleira_esquerda[0] + 5 and
        posicao_goleira_esquerda[1] <= posicao_bola[1] <= posicao_goleira_esquerda[1] + 300):
        pontos_jogador_direito += 1 # Contador de gols
        if pontos_jogador_direito == 10: # Condição para fim do jogo
            print("Jogador Direito Venceu!")
            pygame.quit()
            return
        posicao_bola = [largura_tela // 2, altura_tela // 2]  # Reseta a posição da bola
        direcao_bola[0] *= -1 # Faz com que a bola vá na direção contrária
            
    if  (posicao_bola[0] + tamanho_bola / 2 >= posicao_goleira_direita[0] - 5 and posicao_goleira_direita[1] <= posicao_bola[1] <= posicao_goleira_direita[1] + 300):
        pontos_jogador_esquerdo += 1 # Contador de gols
        if pontos_jogador_esquerdo == 10: # Condição para fim do jogo
            print("Jogador Esquerdo Venceu!")
            pygame.quit()
            return
        posicao_bola = [largura_tela // 2, altura_tela // 2]  # Reseta a posição da bola
        direcao_bola[0] *= -1 # Faz com que a bola vá na direção contrária

# Função principal
def main():
    pygame.init()
    # Obtem as dimensões da tela do monitor
    largura_monitor = pygame.display.Info().current_w
    altura_monitor = pygame.display.Info().current_h
    # Calcula as coordenadas de início da janela para centralizá-la
    posicao_x = (largura_monitor - largura_tela) // 2
    posicao_y = (altura_monitor - altura_tela) // 2
    tela = pygame.display.set_mode((largura_tela, altura_tela), FULLSCREEN) # Faz com a tela fique em fullscreen
    pygame.display.set_caption("Jogo de Pong Versão Futebolística")
    # Atualiza a janela para exibi-la centralizada
    pygame.display.update()
    
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        # Movimento do jogador esquerdo
        if keys[K_w] and posicao_jogador_esquerdo[1] > 0:
            posicao_jogador_esquerdo[1] -= velocidade_jogador
        elif keys[K_s] and posicao_jogador_esquerdo[1] < altura_tela - altura_jogador:
            posicao_jogador_esquerdo[1] += velocidade_jogador

        # Movimento do jogador direito
        if keys[K_i] and posicao_jogador_direito[1] > 0:
            posicao_jogador_direito[1] -= velocidade_jogador
        elif keys[K_k] and posicao_jogador_direito[1] < altura_tela - altura_jogador:
            posicao_jogador_direito[1] += velocidade_jogador



        tela.fill((0, 128, 0))  # Aplica uma cor de fundo verde para simular grama
        desenha_retangulo(tela, largura_tela//2 - 4, 0, 8, altura_tela, (0, 0, 0))  # Desenha a linha central que separa o campo
        desenha_circulo_centro(tela, (largura_tela // 2, altura_tela // 2), 100, (0, 0, 0), 8) # Desenha o circulo no centro do campo
        desenha_linhas_bordas(tela, largura_tela, altura_tela, (0, 0, 0))  # Desenha as linhas ao entorno do campo
        desenha_goleiras(tela) # Desenha as goleiras          
        desenha_area_goleira(tela, (0, 0, 0), pygame.Rect(0, altura_tela // 2 - 150, 150, 300)) # Desenha a área na frente da goleira
        desenha_area_goleira(tela, (0, 0, 0), pygame.Rect(largura_tela - 150, altura_tela // 2 - 150, 150, 300)) # Desenha a área na frente da goleira
        desenha_jogadores(tela) # Desenha os jogadores
        desenha_placar(tela)  # Desenha o placar na tela
        desenha_bola(tela) # Desenha a bola
        atualiza_bola() # Atualiza a posição da bola

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
