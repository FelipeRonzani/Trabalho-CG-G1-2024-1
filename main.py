from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Constantes globais
largura_tela = 1280
altura_tela = 720
largura_jogador = 20
altura_jogador = 100
tamanho_bola = 30
velocidade_jogador = 20
velocidade_bola_x = 0.5
velocidade_bola_y = 0.5

# Posições Iniciais
posicao_jogador_esquerdo = [30, altura_tela // 2 - altura_jogador // 2]
posicao_jogador_direito = [largura_tela - 30 - largura_jogador, altura_tela // 2 - altura_jogador // 2]
posicao_bola = [largura_tela // 2, altura_tela // 2]
direcao_bola = [0.5, 0.5]  # Posição da bola inicial

# Função para desenhar um retângulo.
def desenha_retangulo(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()
    
#def goleira()
    # invisivel
    
# Função para desenhar os jogadores.
def desenha_jogadores():
    glColor3f(1.0, 1.0, 0)  
    desenha_retangulo(posicao_jogador_esquerdo[0], posicao_jogador_esquerdo[1], largura_jogador, altura_jogador)
    desenha_retangulo(posicao_jogador_direito[0], posicao_jogador_direito[1], largura_jogador, altura_jogador)

# Função para desenhar a bola.
def desenha_bola():
    glColor3f(1.0, 1.0, 5.0)  
    desenha_retangulo(posicao_bola[0] - tamanho_bola / 2, posicao_bola[1] - tamanho_bola / 2, tamanho_bola, tamanho_bola)

# Função para atualizar a posição da bola.
def atualiza_bola():
    global posicao_bola, direcao_bola

    # Atualiza a posição da bola.
    posicao_bola[0] += direcao_bola[0] * velocidade_bola_x
    posicao_bola[1] += direcao_bola[1] * velocidade_bola_y

    # Colisão da bola com o topo e o fundo da tela. 
    if posicao_bola[1] <= 0 or posicao_bola[1] >= altura_tela:
        direcao_bola[1] *= -1

    # Colisão da bola com os jogadores.
    if (posicao_bola[0] - tamanho_bola / 2 <= posicao_jogador_esquerdo[0] + largura_jogador and
        posicao_jogador_esquerdo[1] <= posicao_bola[1] <= posicao_jogador_esquerdo[1] + altura_jogador):
        direcao_bola[0] *= -1

    if (posicao_bola[0] + tamanho_bola / 2 >= posicao_jogador_direito[0] and
        posicao_jogador_direito[1] <= posicao_bola[1] <= posicao_jogador_direito[1] + altura_jogador):
        direcao_bola[0] *= -1

    # Colisão da bola com os lados esquerdo e direito da tela.
    if posicao_bola[0] <= 0 or posicao_bola[0] >= largura_tela:
        posicao_bola = [largura_tela // 2, altura_tela // 2]  # Reseta a posição da bola.
        
#def placar():
    # desenhar os números de 0 à 9
    # contador esquerdo e direito
    

# Função de teclado.
def teclado(key, x, y):
    global posicao_jogador_esquerdo, posicao_jogador_direito

    if key == b'w' and posicao_jogador_esquerdo[1] < altura_tela - altura_jogador:
        posicao_jogador_esquerdo[1] += velocidade_jogador
    elif key == b's' and posicao_jogador_esquerdo[1] > 0:
        posicao_jogador_esquerdo[1] -= velocidade_jogador
    elif key == b'k' and posicao_jogador_direito[1] < altura_tela - altura_jogador:
        posicao_jogador_direito[1] += velocidade_jogador
    elif key == b'i' and posicao_jogador_direito[1] > 0:
        posicao_jogador_direito[1] -= velocidade_jogador

# Função de display.
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    desenha_jogadores()
    desenha_bola()
    atualiza_bola()
    glutSwapBuffers()

# Função principal.
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(largura_tela, altura_tela)
glutCreateWindow(b"Jogo")

glutDisplayFunc(display)
glutIdleFunc(display)
glutKeyboardFunc(teclado)

glClearColor(0.0, 0.0, 0.0, 1.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, largura_tela, 0, altura_tela, -1, 1)
glMatrixMode(GL_MODELVIEW)

glutMainLoop()
