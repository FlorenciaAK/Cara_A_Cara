# ===== INICIALIZAÇÃO =====

#----------Descrição do jogo
'''
Jogo: Cara A Cara 
Autores: Florencia , Gustavo Borges , Sophia 
'''

#----------importações necessárias
import pygame
import random
import os
import sys

#----------tabela de cores
BRANCO = (255,255,255)
VERMELHO = (255,0,0)
PRETO = (0,0,0)
VERDE = (0,255,0)

#----------dimensões da tela
LARGURA = 1400
ALTURA = 750

#----------uniformiza o tamanho dos Botoes 
largura_botao =90
altura_botao =150


#----------INTRODUÇÃO----------

#----------nomes das personagens
nomes_jogadores = ["Rodrigo", "Karina", "Ricardo", "Bruno", "Paula", "Francisco", "Erica", "Sonia", "Felipe", "Julia", "Eduardo", "Mariana", "Pedro", "Gisele", "Juliana", "Robson","Aline", "Gabriel", "Nathalia", "Daniel", "Marcelo", "João", "Marta", "Renato"]

#----------classe que atribui características as personagens
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

#----------criação dos objetos tipo Carac (personagens)
Rodrigo = Carac('masculino', 'clara', 'castanho', 'fechada', 'castanhos', 'nao', 'nao', 'pontudo', 'nao')
Karina = Carac('feminino', 'negra', 'castanho', 'aberta', 'verdes', 'nao', 'nao', 'redondo', 'brincos')
Ricardo = Carac('masculino', 'clara', 'preto', 'aberta', 'castanhos', 'nao', 'barba', 'redondo', 'nao')
Bruno = Carac('masculino', 'clara', 'loiro', 'fechada', 'verdes', 'sim', 'barba', 'redondo', 'nao')
Paula = Carac('feminino', 'clara', 'loiro', 'fechada', 'castanhos ', 'nao', 'nao', 'redondo', 'batom')
Fransisco = Carac('masculio', 'clara', 'castanho', 'aberta', 'azuis', 'nao', 'bigode', 'pontudo', 'nao')
Erica = Carac('feminino', 'clara', 'loiro', 'fecada', 'azuis', 'sim', 'nao', 'redondo', 'chapeu')
Sonia = Carac('feminino', 'clara', 'branco', 'fechada', 'verdes', 'sim', 'nao', 'pontudo', 'brinco')
Felipe = Carac('masculino', 'clara', 'nao', 'abeta', 'preto', 'oculos', 'bigode', 'pontudo', 'nao')
Julia = Carac('feminino', 'clara', 'castanho', 'fechada', 'pretos', 'nao', 'nao', 'redondo', 'nao')
Eduardo = Carac('masculino' , 'clara', 'loiro', 'aberta', 'azuis', 'nao', 'nao', 'pontudo', 'chapeu')
Mariana = Carac('feminino', 'clara', 'branco', 'fechada', 'castanhos', 'nao', 'nao', 'redondo', 'brinco')
Pedro = Carac('masculino', 'clara', 'preto', 'fechada', 'verdes', 'nao', 'nao', 'redondo', 'bone')
Gisele = Carac('feminino', 'negra', 'preto', 'fechada', 'castanhos', 'nao', 'nao', 'redondo', 'brincos')
Juliana = Carac('feminino', 'clara', 'preto', 'aberta', 'pretos', 'nao', 'nao', 'redondo', 'brincos')
Robson = Carac('masculino', 'negra', 'preto', 'fechada', 'castanho', 'sim', 'nao', 'redondo', 'nao')
Aline = Carac('feminino', 'clara', 'ruivo', 'aberta', 'verdes', 'sim', 'nao', 'pontudo', 'nao')
Gabriel = Carac('masculino', 'negra', 'preto', 'aberta', 'castanhos', 'nao', 'nao', 'pontudo', 'faixa')
Nathalia = Carac('feminino', 'negra', 'preto', 'fechada', 'castanhos', 'nao', 'nao', 'pontudo', 'brincos')
Daniel = Carac('masculino','clara','ruivo','aberta','castanhos','nao','barba','redondo','nao')
Marcelo = Carac('masculino','clara','nao','aberta','pretos','nao','barba','redondo','nao')
Joao = Carac('masculino','clara','branco','fechada','pretos','nao','nao','pontudo','chapeu')
Marta = Carac('feminino','clara','preto','aberta','azuis','nao','nao','redondo','brinco')
Renato = Carac('masculino','clara','preto','fechada','pretos','nao','nao','redondo','nao')

#----------classe que cria os botões das personagens
class button(pygame.sprite.Sprite):
    def __init__(self,nome_da_imagen, x,y):
        #Define o botao importando as sprites das personagens
        self.image = os.path.join('assets/img',nome_da_imagen)
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(largura_botao,altura_botao))
        self.x = x
        self.y = y

    def draw(self,win,outline=None):
        #funcao que desenha o botao na tela 
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,largura_botao+4,altura_botao+4),0)
            
        window.blit(self.image,[self.x,self.y])
        

    def isOver(self, pos):
        #Rastreia a posicao do  mause para  ver se esta em cima do botao
        if pos[0] > self.x and pos[0] < self.x + largura_botao :
            if pos[1] > self.y and pos[1] < self.y + altura_botao:
                return True
            
        return False

#----------criação dos objetos do tipo button, que define um botao para cada uma das personagens
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

#----------função que reseta a tela para seu estado original 
def redesenhaWindow():
        window.fill(BRANCO)
        Aline_button.draw(window,PRETO)
        Rodrigo_button.draw(window,PRETO) 
        Karina_button.draw(window,PRETO)
        Ricardo_button.draw(window,PRETO)
        Bruno_button.draw(window,PRETO)
        Paula_button.draw(window,PRETO)
        Fransisco_button.draw(window,PRETO)
        Erica_button.draw(window,PRETO)
        Sonia_button.draw(window,PRETO) 
        Felipe_button.draw(window,PRETO)
        Julia_button.draw(window,PRETO)
        Eduardo_button.draw(window,PRETO) 
        Mariana_button.draw(window,PRETO)
        Pedro_button.draw(window,PRETO)
        Gisele_button.draw(window,PRETO)
        Juliana_button.draw(window,PRETO)
        Robson_button.draw(window,PRETO)
        Gabriel_button.draw(window,PRETO)
        Nathalia_button.draw(window,PRETO)
        Daniel_button.draw(window,PRETO)
        Marcelo_button.draw(window,PRETO)
        Joao_button.draw(window,PRETO)
        Marta_button.draw(window,PRETO)
        Renato_button.draw(window,PRETO)

#----------função que da load nos sons do jogo:
cache_sons = {}  
def carrega_sons (som):
    if not som in cache_sons:
        try:
            caminho = os.path.join(os.path.dirname(__file__ ), som)
            cache_sons[som] = pygame.mixer.Sound(caminho)
            cache_sons[som].set_volume(0.1)

        except pygame.error:
            print('Erro ao tentar reproduzir: {0}.ogg'.format(som))
            sys.exit()

        return cache_sons[som]

#----------funçao principal:
def main():  
    """Rotina principal do jogo Cara A Cara de pygame"""

    #----------inicia rotinas do pygame
    pygame.init()

    #----------cria superfície de jogo
    window = pygame.display.set_mode((LARGURA,ALTURA))

    #----------cria título do jogo
    pygame.display.set_caption("CARA A CARA")

    #----------musica de fundo:
    arquivo = os.path.join("assets/sons", "ghost_town.ogg")
    caminho = os.path.join(os.path.dirname(__file__ ), arquivo)
    pygame.mixer.music.load(caminho)
    pygame.mixer.set_volume(0.3)
    pygame.mixer.music.play(-1)

    #----------tela inicial
    inicio_dir = os.path.join("assets/img','inicio.jpeg")
    inicio_load = pygame.image.load(inicio_dir).convert()
    inicio = pygame.transform.scale(inicio_load, (LARGURA, ALTURA))
    window.blit(inicio, (0,0))
    pygame.display.update() 

    #----------variável que define quando o jogo acaba
    game = False

    #----------variável de FPS máxima em Hz
    FPS = 60

    #----------variavel da posicao do mouse
    pos = pygame.mouse.get_pos()

    # #----------verifica se o jogador clicou em alguma tecla do teclado
    # if event.type == pygame.KEYDOWN:
    #     game = True 

    #----------inicia contador de tentativas
    contador = 1

    # ===== Loop principal =====

    while game == True:
        #----------garante uma FPS máxima de 60 Hz
        delta_time = clock.tick(FPS)

        #----------chamando a função que redesenha todos os botões
        redesenhaWindow()
        pygame.display.update()

        #----------jogadores sorteados
        jogador_sorteio_i = random.randint(0,len(nomes_jogadores))
        jogador_escolhido = nomes_jogadores [jogador_sorteio_i]

        #----------coleta de eventos
        eventos = pygame.event.get()
        for evento in eventos:
            #----------evento para sair do jogo
            if event.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
                game = False
                pygame.quit()              
                sys.exit() 

            #----------evento que verifica se o botão do mouse foi clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Aline_button.isOver(pos):
                    print('botao clicado')
                if Rodrigo_button.isOver(pos):
                    print('botao clicado')
                if Karina_button.isOver(pos):
                    print('botao clicado')
                if Ricardo_button.isOver(pos):
                    print('botao clicado')
                if Bruno_button.isOver(pos):
                    print('botao clicado')
                if Paula_button.isOver(pos):
                    print('botao clicado')
                if Fransisco_button.isOver(pos):
                    print('botao clicado')
                if Erica_button.isOver(pos):
                    print('botao clicado')
                if Sonia_button.isOver(pos):
                    print('botao clicado')
                if Felipe_button.isOver(pos):
                    print('botao clicado')
                if Julia_button.isOver(pos):
                    print('botao clicado')
                if Eduardo_button.isOver(pos):
                    print('botao clicado')
                if Mariana_button.isOver(pos):
                    print('botao clicado')
                if Pedro_button.isOver(pos):
                    print('botao clicado')
                if Gisele_button.isOver(pos):
                    print('botao clicado')
                if Juliana_button.isOver(pos):
                    print('botao clicado')
                if Robson_button.isOver(pos):
                    print('botao clicado')
                if Gabriel_button.isOver(pos):
                    print('botao clicado')
                if Nathalia_button.isOver(pos):
                    print('botao clicado')
                if Daniel_button.isOver(pos):
                    print('botao clicado')
                if Marcelo_button.isOver(pos):
                    print('botao clicado')
                if Joao_button.isOver(pos):
                    print('botao clicado')
                if Marta_button.isOver(pos):
                    print('botao clicado')
                if Renato_button.isOver(pos):
                    print('botao clicado')
                

        #----------preenche tela com cor branca
        window.fill(BRANCO)

        #----------atualiza a tela
        pygame.display.flip()

#----------função main
if __name__ == ' __main__': 
    main()