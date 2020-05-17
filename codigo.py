# ===== Inicialização =====

#importações necessárias
import pygame
import random
from os import path

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
Karina = Carac(feminino, negra, castanho, aberta, verdes, nao, nao, redondo, brincos)
Ricardo = Carac(masculino, clara, preto, aberta, castanhos, nao, barba, redondo, nao)
Bruno = Carac(masculino, clara, loiro, fechada, verdes, sim, barba, redondo, nao)
Paula = Carac(feminino, clara, loiro, fechada, castanhos, nao, nao, redondo, batom)
Fransisco = Carac(masculio, clara, castanho, aberta, azuis, nao, bigode, pontudo, nao)
Erica = Carac(feminino, clara, loiro, fecada, azuis, sim, nao, redondo, chapeu)
Sonia = Carac(feminino, clara, branco, fechada, verdes, sim, nao, pontudo, brinco)
Felipe = Carac(masculino, clara, nao, abeta, preto, oculos, bigode, pontudo, nao)
Julia = Carac(feminino, clara, castanho, fechada, pretos, nao, nao, redondo, nao)
Eduardo = Carac(masculino , clara, loiro, aberta, azuis, nao, nao, pontudo, chapeu)
Mariana = Carac(feminino, clara, branco, fechada, castanhos, nao, nao, redondo, brinco)
Pedro = Carac(masculino, clara, preto, fechada, verdes, nao, nao, redondo, bone)
Gisele = Carac(feminino, negra, preto, fechada, castanhos, nao, redondo, brincos)
Juliana = Carac(feminino, clara, preto, aberta, pretos, nao, nao, redondo, brincos)
Robson = Carac(masculino, negra, preto, fechada, castanho, sim, nao, redondo, nao)
Aline = Carac(feminino, clara, ruivo, aberta, verdes, sim, nao, pontudo, nao)
Gabriel = Carac(masculino, negra, preto, aberta, castanhos, nao, nao, pontudo, faixa)
Nathalia = Carac(feminino, negra, preto, fechada, castanhos, nao, nao, pontudo, brincos)
Daniel = Carac(masculino,clara,ruivo,aberta,castanhos,nao,barba,redondo,nao)
Marcelo = Carac(masculino,clara,nao,aberta,pretos,nao,barba,redondo,nao)
Joao = Carac(masculino,clara,branco,fechada,pretos,nao,nao,pontudo,chapeu)
Marta = Carac(feminino,clara,preto,aberta,azuis,nao,nao,redondo,brinco)
Renato = Carac(masculino,clara,preto,fechada,pretos,nao,nao,redondo,nao)

#tela inicial
inicio_dir = path.join(path.dirname(__file__),'assets/img')
inicio_load = pygame.image.load(path.join(inicio_dir, 'inicio.png')).convert()
inicio = pygame.transform.scale(inicio_load, (LARGURA, ALTURA))
window.blit(inicio, (0,0))


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
        #verifica se o jogador clicou em alguma tecta do teclado
        if event.type == pygame.key.get_press():
            

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