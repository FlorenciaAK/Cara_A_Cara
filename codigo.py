# ===== Inicialização =====

#importações necessárias
import pygame
import random

#inicio pacote do pygame
pygame.init()

# ----- Gera tela principal
#cria tela com 1400 pixels de largura e 750 pixels de altura
LARGURA = 1400
ALTURA = 750
window = pygame.display.set_mode((LARGURA,ALTURA))

#define o título da janela
pygame.display.set_caption ("Cara a cara")



# ===== Loop principal =====
nomes_jogadores = ["Rodrigo", "Karina", "Ricardo", "Bruno", "Paula", "Francisco", "Erica", "Sonia", "Felipe", "Julia", "Eduardo", "Mariana", "Pedro", "Gisele", "Juliana", "Robson","Aline", "Gabriel", "Nathalia", "Daniel", "Marcelo", "João", "Marta", "Renato"]
jogador_escolhido_i = random.randint(0,len(nomes_jogaodes))
jogador_certo = nomes_jogadores [jogador_escolhido_i]

class Carac:
    def __init__ (self, sexo, cor_pele, cor_cabelo, tipo_boca, cor_olho, oculos, pelo_facial, queixo, acessorios):
        self.sexo = sexo
        self.cor_pele = cor_pele
        self.cor_cabelo = cor_cabelo
        self.tipo_boca = tipo_boca
        self.cor_olho = cor_olho
        self.oculos = oculos
        self.pelo_facial = pelo_facial
        self.queixo = queixo
        self.acessorios = acessorios

Rodrigo = Carac(masculino, clara, castanho, fechada, castanhos, nao, nao, pontudo, nao)
Karina = Carac(femenino, negra, castanho, aberta, verde, nao, nao, redondo, brincos)
Ricardo = Carac(masculino, clara, preto, aberta, castanhos, nao, barba, redondo, nao)
Bruno = Carac(masculino, clara, loiro, fechada, verdes, sim, barba, redondo, nao)

#variável game que define que o jogo deve continuar
game = True

#inicia contador de tentativas
contador = 1

#continua o jogo enquanto game for True
while game:
    #pygame.event.get() devolve uma lista com todos os eventos que ocorreram desde a última vez q a funçao foi chamada (get())
    for event in pygame.event.get():
        #verifica se o tipo de evento é pygame.QUIT (se o usuário clicou no botão de fechar a janela)
        if event.type == pygame.QUIT:
                game = False

    #preenche tela com cor branca
    window.fill((255, 255, 255))

    #perguntar se o jogador que chutar um nome
    
    desejo = input("Você quer chutar algum nome? s ou n: ")
        if desejo == "s":
            def chute ():
                chute = input("Quem?:")
                if chute == jogador_certo:
                    return ("Você acertou após {0} tentativas".format(contador))
                    game = False
                else:
                    continue
                    game = True

    #mostrar nova tela que foi desenhada ao usuário
    pygame.display.update()





# ===== Finalização =====

#print ("você ganhou depois de {0} tentativas".format(contador))
#finaliza o pygame (fecha todos os recursos que abriu)
pygame.quit()