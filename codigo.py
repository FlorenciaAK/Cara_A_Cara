# ===== Inicialização =====

#importações necessárias
import pygame
import random

#inicio pacote do pygame
pygame.init()

# ----- Gera tela principal
#cria tela com 500 pixels de largura e 400 pixels de altura
window = pygame.display.set_mode((500,400))

#define o título da janela
pygame.display.set_caption ("Cara a cara")




# ===== Loop principal =====

#variável game que define que o jogo deve continuar
game = True

#continua o jogo enquanto game for True
while game:
    #pygame.event.get() devolve uma lista com todos os eventos que ocorreram desde a última vez q a funçao foi chamada (get())
    for event in pygame.event.get():
        #verifica se o tipo de evento é pygame.KEYUP (se o usuário clicou em qualquer tecla)
        if event.type == pygame.KEYUP:
                game = False

    #preenche tela com cor branca
    window.fill((255, 255, 255))

    #mostrar nova tela que foi desenhada ao usuário
    pygame.display.update()




# ===== Finalização =====

#finaliza o pygame (fecha todos os recursos que abriu)
pygame.quit()