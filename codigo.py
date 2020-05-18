# ===== Inicialização =====

#importações necessárias
import pygame
import random
import os

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

# uniformiza o tamanho dos Botoes 
largura_img =90
altura_img =150
class button(pygame.sprite.Sprite):
    def __init__(self,nome_da_imagen, x,y):
        #Define o botao importando as sprites das personagens
        self.image = os.path.join('Cara_A_Cara','assets','img',nome_da_imagen)
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(largura_img,altura_img))
        self.x = x
        self.y = y

    def draw(self,win,outline=None):
        #funcao que desenha o botao na tela 
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,largura_img+4,altura_img+4),0)
            
        window.blit(self.image,[self.x,self.y])
        

    def isOver(self, pos):
        #Rastreia a posicao do  mause para  ver se esta em cima do botao
        if pos[0] > self.x and pos[0] < self.x + largura_img :
            if pos[1] > self.y and pos[1] < self.y + altura_img:
                return True
            
        return False

#define um botao para cada uma das personagens
Aline_button = button('Aline.jpg',10,20)
Rodrigo_button = button('Rodrigo.jpg',10,206)
Karina_button = button('Karina.jpg',10,392)
Ricardo_button = button('Ricardo.jpg',10,578)
Bruno_button = button('Bruno.jpg',110,20)
Paula_button = button('Paula.jpg',110,206)
Fransisco_button = button('Francisco.jpg',110,392)
Erica_button = button('Erica.jpg',110,578)
Sonia_button = button('Sonia.jpg',210,20)
Felipe_button = button('Felipe.jpg',210,206)
Julia_button = button('Julia.jpg',210,392)
Eduardo_button = button('Eduardo.jpg',210,578)
Mariana_button = button('Mariana.jpg',310,20)
Pedro_button =button('Pedro.jpg',310,206)
Gisele_button = button('Gisele.jpg',310,392)
Juliana_button = button('Juliana.jpg',310,578)
Robson_button = button('Robson.jpg',410,20)
Gabriel_button = button('Gabriel.jpg',410,206)
Nathalia_button = button('Nathalia.jpg',410,392)
Daniel_button = button('Daniel.jpg',410,578)
Marcelo_button =button('Marcelo.jpg',510,20)
Joao_button = button('Joao.jpg',510,206)
Marta_button = button('Marta.jpg',510,392)
Renato_button = button('Renato.jpg',510,578)


#definindo funções:
def chute ():
    chute = input("Quem?:")
    if chute == jogador_certo:
        return ("Você acertou após {0} tentativas".format(contador))
        game = False
    else:
        continue
        game = True

#funcao que reseta a tela para seu estado original 
def redesenhaWindow():
        window.fill((255, 255, 255))
        Aline_button.draw(window,(0,0,0))
        Rodrigo_button.draw(window,(0,0,0)) 
        Karina_button.draw(window,(0,0,0))
        Ricardo_button.draw(window,(0,0,0))
        Bruno_button.draw(window,(0,0,0))
        Paula_button.draw(window,(0,0,0))
        Fransisco_button.draw(window,(0,0,0))
        Erica_button.draw(window,(0,0,0))
        Sonia_button.draw(window,(0,0,0)) 
        Felipe_button.draw(window,(0,0,0))
        Julia_button.draw(window,(0,0,0))
        Eduardo_button.draw(window,(0,0,0)) 
        Mariana_button.draw(window,(0,0,0))
        Pedro_button.draw(window,(0,0,0))
        Gisele_button.draw(window,(0,0,0))
        Juliana_button.draw(window,(0,0,0))
        Robson_button.draw(window,(0,0,0))
        Gabriel_button.draw(window,(0,0,0))
        Nathalia_button.draw(window,(0,0,0))
        Daniel_button.draw(window,(0,0,0))
        Marcelo_button.draw(window,(0,0,0))
        Joao_button.draw(window,(0,0,0))
        Marta_button.draw(window,(0,0,0))
        Renato_button.draw(window,(0,0,0))

#tela inicial
inicio_dir = os.path.join('assets','img','inicio.jpg')
inicio_load = pygame.image.load(inicio_dir).convert()
inicio = pygame.transform.scale(inicio_load, (LARGURA, ALTURA))
window.blit(inicio, (0,0))
 pygame.display.update()



#variável game que define que o jogo deve continuar
game = True


#inicia contador de tentativas
contador = 1

#continua o jogo enquanto game for True
while game:
    redesenhaWindow()
    pygame.display.update()
    #pygame.event.get() devolve uma lista com todos os eventos que ocorreram desde a última vez q a funçao foi chamada (get())
    for event in pygame.event.get():
        #verifica se o tipo de evento é pygame.QUIT (se o usuário clicou no botão de fechar a janela)
        if event.type == pygame.QUIT:
            game = False
        #verifica se o jogador clicou em alguma tecta do teclado
        if event.type == pygame.KEYDOWN:
        #Variavel da posicao do mause
        pos = pygame.mouse.get_pos()
            

    #preenche tela com cor branca
    window.fill((255, 255, 255))

    
    #perguntar se o jogador que chutar um nome
    
    desejo = input("Você quer chutar algum nome? s ou n: ")
    if desejo == "s":
        chute()

    #mostrar nova tela que foi desenhada ao usuário
    pygame.display.update()





# ===== Finalização =====

#print ("você ganhou depois de {0} tentativas".format(contador))
#finaliza o pygame (fecha todos os recursos que abriu)
pygame.quit()