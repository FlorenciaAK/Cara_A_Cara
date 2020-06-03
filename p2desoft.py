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
AZUL =(0,0,255)

#----------dimensões da tela
LARGURA = 1400
ALTURA = 750

#----------uniformiza o tamanho dos Botoes 
largura_botao = 90
altura_botao = 150

#----------uniformiza o tamanho do rosto neutro
largura_pn = 400
altura_pn = 300

#----------uniformiza o tamanho dos botões das características a serem escolhidas
largura_carac = 70
altura_carac = 40

#----------função que da load nos sons do jogo:
cache_sons = {}  
def carrega_sons (som):
    if not som in cache_sons:
        try:
            caminho = os.path.join(os.path.dirname(__file__), som)
            cache_sons[som] = pygame.mixer.Sound(caminho)
            cache_sons[som].set_volume(2)

        except pygame.error:
            print('Erro ao tentar reproduzir: {0}.ogg'.format(som))
            sys.exit()

        return cache_sons[som]

#----------função que da load nas imagens do jogo:
cache_imagens = {}  
def carrega_imagens (imagem):
    if not imagem in cache_imagens:
        try:
            caminho = os.path.join(os.path.dirname(__file__), imagem)
            cache_imagens[imagem] = pygame.image.load(caminho).convert_alpha()

        except pygame.error:
            print('Erro ao tentar load: {0}'.format(imagem))
            sys.exit()

        return cache_imagens[imagem]

#----------classe que atribui características às personagens
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

#----------classe que cria os botões das personagens
class Button(pygame.sprite.Sprite):
    def __init__(self,nome_da_imagem, x,y):

        #----------Define o botão importando as sprites das personagens
        arquivo = os.path.join("assets","img",nome_da_imagem)
        self.image = carrega_imagens(arquivo)
        self.image = pygame.transform.scale(self.image,(largura_botao,altura_botao))
        #----------ponto superior esquerdo da imagem
        self.x = x
        self.y = y
        #----------variável que adiciona ou retira o x em cima da personagem
        self.selecionada = False

    #----------função que desenha o botao na tela 
    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,largura_botao+4,altura_botao+4),0)
            
        win.blit(self.image,[self.x,self.y])

        if self.selecionada:
            pygame.draw.line(win, PRETO, (self.x-2,self.y-2), (self.x+largura_botao, self.y+altura_botao), 5)   
            pygame.draw.line(win, PRETO, (self.x+largura_botao,self.y-2), (self.x-2, self.y+altura_botao), 5) 
    
    #----------função que retorna se o mouse está em cima de certo botão
    def isOver(self, pos):
        #Rastreia a posicao do  mause para  ver se esta em cima do botao
        if pos[0] > self.x and pos[0] < self.x + largura_botao :
            if pos[1] > self.y and pos[1] < self.y + altura_botao:
                return True
        return False

#----------classe que cria os botões das settings
class Settings:
    def __init__(self, color, x, y, width, height, text='', tam_fonte):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.tamanho_da_fonte = tam_fonte

    def draw(self, win, outline=None, tam_fonte):
        #----------Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
    
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont("TimesNewRoman", self.tamanho_da_fonte)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    #----------função que retorna se o mouse está em cima de certo botão
    def isOver(self, pos):
        #----------Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

#----------função principal:
def main():  
    """Rotina principal do jogo Cara A Cara de pygame"""

    #----------inicia rotinas do pygame
    pygame.init()

    #----------cria superfície de jogo
    window = pygame.display.set_mode((LARGURA,ALTURA))

    #----------cria título do jogo
    pygame.display.set_caption("CARA A CARA")

    #----------criação dos objetos tipo Carac (personagens)
    Rodrigo = Carac('masculino', 'clara', 'castanho', 'fechada', 'castanhos', 'nao', 'nao', 'pontudo', 'nao')
    Karina = Carac('feminino', 'negra', 'castanho', 'aberta', 'verdes', 'nao', 'nao', 'redondo', 'brincos')
    Ricardo = Carac('masculino', 'clara', 'preto', 'aberta', 'castanhos', 'nao', 'barba', 'redondo', 'nao')
    Bruno = Carac('masculino', 'clara', 'loiro', 'fechada', 'verdes', 'sim', 'barba', 'redondo', 'nao')
    Paula = Carac('feminino', 'clara', 'loiro', 'fechada', 'castanhos ', 'nao', 'nao', 'redondo', 'batom')
    Francisco = Carac('masculino', 'clara', 'castanho', 'aberta', 'azuis', 'nao', 'bigode', 'pontudo', 'nao')
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

    #----------criação dos objetos do tipo button, que define um botao para cada uma das personagens
    Aline_button = Button('Aline.jpg',10,20)
    Rodrigo_button = Button('Rodrigo.jpg',10,206)
    Karina_button = Button('Karina.jpg',10,392)
    Ricardo_button = Button('Ricardo.jpg',10,578)
    Bruno_button = Button('Bruno.jpg',110,20)
    Paula_button = Button('Paula.jpg',110,206)
    Francisco_button = Button('Francisco.jpg',110,392)
    Erica_button = Button('Erica.jpg',110,578)
    Sonia_button = Button('Sonia.jpg',210,20)
    Felipe_button = Button('Felipe.jpg',210,206)
    Julia_button = Button('Julia.jpg',210,392)
    Eduardo_button = Button('Eduardo.jpg',210,578)
    Mariana_button = Button('Mariana.jpg',310,20)
    Pedro_button = Button('Pedro.jpg',310,206)
    Gisele_button = Button('Gisele.jpg',310,392)
    Juliana_button = Button('Juliana.jpg',310,578)
    Robson_button = Button('Robson.jpg',410,20)
    Gabriel_button = Button('Gabriel.jpg',410,206)
    Nathalia_button = Button('Nathalia.jpg',410,392)
    Daniel_button = Button('Daniel.jpg',410,578)
    Marcelo_button = Button('Marcelo.jpg',510,20)
    Joao_button = Button('Joao.jpg',510,206)
    Marta_button = Button('Marta.jpg',510,392)
    Renato_button = Button('Renato.jpg',510,578)

    #----------criação dos objetos do tipo settings
    Regras = Settings(VERMELHO, 150 , 300, 400, 200,'Regras',60) 
    Inicio = Settings(VERDE, 850 , 300, 400, 200,'Iniciar',60)
    Chutar = Settings(AZUL,1000,20,200,100,'Chutar', 60)

    #----------criação dos objetos do tipo setting, que define um botao para cada uma das características
    sexo_button = Settings(VERDE, 750, 300, largura_carac, altura_carac,'Sexo', 20)
    pele_button = Settings(VERDE, 1000, 200, largura_carac, altura_carac,'Cor da pele', 20)
    cabelo_button = Settings(VERDE, 500, 200, largura_carac, altura_carac,'Cor do cabelo', 20)
    boca_button = Settings(VERDE, 1000, 200, largura_carac, altura_carac,'Tipo de boca', 20)
    olho_button = Settings(VERDE, 1000, 200, largura_carac, altura_carac,'Cor do olho', 20)
    oculo_button = Settings(VERDE, 500, 200, largura_carac, altura_carac,'Óculos', 20)
    barba_button = Settings(VERDE, 500, 200, largura_carac, altura_carac,'Pelo facial', 20)
    queixo_button = Settings(VERDE, 1000, 200, largura_carac, altura_carac,'Tipo de queixo', 20)
    acessorios_button = Settings(VERDE, 500, 200, largura_carac, altura_carac,'Acessórios', 20)

    #----------música de fundo
    arquivo = os.path.join("assets","sons", "ghost_town.ogg")
    caminho = os.path.join(os.path.dirname(__file__), arquivo)
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    #----------variável que armazena som quando o X é adicionado
    arquivo_x = os.path.join('assets','sons','som_do_x.ogg')
    som_x = carrega_sons(arquivo_x)

    #----------tela inicial
    inicio_dir = os.path.join("assets","img",'inicio.jpeg')  #########criar imagem de inicio
    inicio_load = pygame.image.load(inicio_dir).convert()
    inicio = pygame.transform.scale(inicio_load, (LARGURA, ALTURA))
    window.blit(inicio, (0,0))

    #----------Cria os Bottoes de Inicio e Regras
    Regras.draw(window,PRETO)
    Inicio.draw(window,PRETO)
    pygame.display.update()

    #----------Base Para Box Input
    fonte_base = pygame.font.Font(None,32)
    user_text = '' 
    largura_input = 140
    input_rect = pygame.Rect(1000,140,largura_input,32)
    draw_input = False

    #----------nomes das personagens
    nomes_personagens = ["Rodrigo", "Karina", "Ricardo", "Bruno", "Paula", "Francisco", "Erica", "Sonia", "Felipe", "Julia", "Eduardo", "Mariana", "Pedro", "Gisele", "Juliana", "Robson","Aline", "Gabriel", "Nathalia", "Daniel", "Marcelo", "João", "Marta", "Renato"] 
    #----------personagens sorteados
    personagem_sorteio_i = random.randrange(0,len(nomes_personagens))
    personagem_escolhido = nomes_personagens [personagem_sorteio_i]
    personagem_escolhido_lower = personagem_escolhido.lower()
    print(personagem_escolhido)

    #----------variável que define quando o jogo acaba
    game = False

    #----------tela de regras
    regras_dir = os.path.join("assets","img",'regras.jpeg')  #########criar imagem de regras 
    regras_load = carrega_imagens(regras_dir)
    regras = pygame.transform.scale(regras_load, (LARGURA, ALTURA))

    #----------imagem da pessoa neutra
    pessoa_neutra_dir = os.path.join("assets","img","rosto_neutro.jpeg")
    pessoa_neutra_load = carrega_imagens(pessoa_neutra_dir)
    pessoa_neutra = pygame.transform.scale(pessoa_neutra_load,(largura_pn, altura_pn))

    #----------objeto para controle da atualização de imagens   
    FPS = 60
    clock = pygame.time.Clock()

    #----------identificar se o botão chute foi apertado
    cor_bativa = AZUL
    cor_bpassiva = PRETO
    active = False

    #----------contador de tentativas
    contador = 5

    #----------começa a interção com o jogador----------
    #----------verifica se o jogador clicou em algum botão e direciona para tela especifica
    while True:
        #----------Marca um ritmo pro computador funcionar
        clock.tick(FPS)

        #----------não faz nada até certo event acontecer
        event = pygame.event.wait()

        #----------devolve uma lista com os acontecimentos do teclado e mouse
        eventos = pygame.event.get()

        #----------variavel da posição do mouse
        pos = pygame.mouse.get_pos()
        print (pos)

        #----------percorre a lista de eventos
        for evento in eventos:
            #----------verifica se o jogador clicou no x vermelho da tela
            if evento.type == pygame.QUIT: 
                game = False
                pygame.quit()              
                sys.exit() 

        #----------verifica se o mouse está sobre o botão iniciar e se este foi clicado
        if event.type == pygame.MOUSEBUTTONDOWN and Inicio.isOver(pos):
            game = True
            break
        
        #----------verifica se o mouse está sobre o botão regras e se este foi clicado
        if event.type == pygame.MOUSEBUTTONDOWN and Regras.isOver(pos):
            window.blit(regras, (0,0))
            #----------verifica se o jogador clicou em qualquer tecla para iniciar o jogo 
            if event.type == pygame.KEYDOWN:
                game = True
                break

    while game and (contador > 0):
        #----------Marca um ritmo pro computador funcionar
        clock.tick(FPS)
        
        #----------preenche tela com cor branca
        window.fill(BRANCO)

        #----------coloca a quantidade de chutes restantes na tela:
        font = pygame.font.SysFont("TimesNewRoman", 30)
        texto = font.render("Tentativas restantes: {0}".format(contador), True, PRETO)

        #----------Desenha os rosto neutro
        window.blit(pessoa_neutra,(800,350))

        #----------Desenha os botões das personagens
        Aline_button.draw(window,PRETO)
        Rodrigo_button.draw(window,PRETO) 
        Karina_button.draw(window,PRETO)
        Ricardo_button.draw(window,PRETO)
        Bruno_button.draw(window,PRETO)
        Paula_button.draw(window,PRETO)
        Francisco_button.draw(window,PRETO)
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
        Chutar.draw(window,PRETO)

        #----------Desenha os botões das características
        sexo_button.draw(window,PRETO)
        pele_button.draw(window,PRETO)
        cabelo_button.draw(window,PRETO)
        boca_button.draw(window,PRETO)
        olho_button.draw(window,PRETO)
        oculos_button.draw(window,PRETO)
        barba_button.draw(window,PRETO)
        queixo_button.draw(window,PRETO)
        acessorios_button.draw(window,PRETO)

        #----------variável da posição do mouse
        pos = pygame.mouse.get_pos()

        #----------coleta de eventos
        eventos = pygame.event.get()

        #----------percorre a lista de eventos
        for event in eventos:
            #----------evento para sair do jogo
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                game = False
                pygame.quit()              
                sys.exit() 

            #----------evento que verifica se o botão do mouse foi clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Aline_button.isOver(pos):
                    if Aline_button.selecionada == False:
                        Aline_button.selecionada = True
                    elif Aline_button.selecionada == True:
                        Aline_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Rodrigo_button.isOver(pos):
                    if Rodrigo_button.selecionada == False:
                        Rodrigo_button.selecionada = True
                    elif Rodrigo_button.selecionada == True:
                        Rodrigo_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Karina_button.isOver(pos):
                    if Karina_button.selecionada == False:
                        Karina_button.selecionada = True
                    elif Karina_button.selecionada == True:
                        Karina_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Ricardo_button.isOver(pos):
                    if Ricardo_button.selecionada == False:
                        Ricardo_button.selecionada = True
                    elif Ricardo_button.selecionada == True:
                        Ricardo_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Bruno_button.isOver(pos):
                    if Bruno_button.selecionada == False:
                        Bruno_button.selecionada = True
                    elif Bruno_button.selecionada == True:
                        Bruno_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Paula_button.isOver(pos):
                    if Paula_button.selecionada == False:
                        Paula_button.selecionada = True
                    elif Paula_button.selecionada == True:
                        Paula_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Francisco_button.isOver(pos):
                    if Francisco_button.selecionada == False:
                        Francisco_button.selecionada = True
                    elif Francisco_button.selecionada == True:
                        Francisco_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Erica_button.isOver(pos):
                    if Erica_button.selecionada == False:
                        Erica_button.selecionada = True
                    elif Erica_button.selecionada == True:
                        Erica_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Sonia_button.isOver(pos):
                    if Sonia_button.selecionada == False:
                        Sonia_button.selecionada = True
                    elif Sonia_button.selecionada == True:
                        Sonia_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Felipe_button.isOver(pos):
                    if Felipe_button.selecionada == False:
                        Felipe_button.selecionada = True
                    elif Felipe_button.selecionada == True:
                        Felipe_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Julia_button.isOver(pos):
                    if Julia_button.selecionada == False:
                        Julia_button.selecionada = True
                    elif Julia_button.selecionada == True:
                        Julia_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Eduardo_button.isOver(pos):
                    if Eduardo_button.selecionada == False:
                        Eduardo_button.selecionada = True
                    elif Eduardo_button.selecionada == True:
                       Eduardo_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Mariana_button.isOver(pos):
                    if Mariana_button.selecionada == False:
                        Mariana_button.selecionada = True
                    elif Mariana_button.selecionada == True:
                        Mariana_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Pedro_button.isOver(pos):
                    if Pedro_button.selecionada == False:
                        Pedro_button.selecionada = True
                    elif Pedro_button.selecionada == True:
                        Pedro_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Gisele_button.isOver(pos):
                    if  Gisele_button.selecionada == False:
                         Gisele_button.selecionada = True
                    elif  Gisele_button.selecionada == True:
                         Gisele_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Juliana_button.isOver(pos):
                    if Juliana_button.selecionada == False:
                        Juliana_button.selecionada = True
                    elif Juliana_button.selecionada == True:
                        Juliana_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Robson_button.isOver(pos):
                    if  Robson_button.selecionada == False:
                        Robson_button.selecionada = True
                    elif Robson_button.selecionada == True:
                        Robson_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Gabriel_button.isOver(pos):
                    if Gabriel_button.selecionada == False:
                        Gabriel_button.selecionada = True
                    elif Gabriel_button.selecionada == True:
                        Gabriel_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Nathalia_button.isOver(pos):
                    if Nathalia_button.selecionada == False:
                        Nathalia_button.selecionada = True
                    elif Nathalia_button.selecionada == True:
                        Nathalia_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Daniel_button.isOver(pos):
                    if Daniel_button.selecionada == False:
                        Daniel_button.selecionada = True
                    elif Daniel_button.selecionada == True:
                        Daniel_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Marcelo_button.isOver(pos):
                    if Marcelo_button.selecionada == False:
                        Marcelo_button.selecionada = True
                    elif Marcelo_button.selecionada == True:
                        Marcelo_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Joao_button.isOver(pos):
                    if Joao_button.selecionada == False:
                        Joao_button.selecionada = True
                    elif Joao_button.selecionada == True:
                        Joao_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Marta_button.isOver(pos):
                    if Marta_button.selecionada == False:
                        Marta_button.selecionada = True
                    elif Marta_button.selecionada == True:
                        Marta_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                if Renato_button.isOver(pos):
                    if Renato_button.selecionada == False:
                       Renato_button.selecionada = True
                    elif Renato_button.selecionada == True:
                        Renato_button.selecionada = False
                    print('botao clicado')
                    som_x.play()
                #----------evento que verifica se o jogador clicou no botão chute
                if Chutar.isOver(pos):
                    draw_input = True
                #----------evento ?????????
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            #----------evento que permite realizar o chute
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        user_text_lower = user_text.lower()
                        if user_text_lower == personagem_escolhido_lower:
                            #----------tela do vencedor
                            venceu_dir = os.path.join("assets","img",'Tela_ganhadora.jpeg')  #########criar imgame de regras 
                            venceu_load = carrega_imagens(venceu_dir)
                            venceu = pygame.transform.scale(venceu_load, (LARGURA, ALTURA))
                            window.blit(venceu, (0, 0))
                        else:
                            contador -= 1
                            

                    else:
                        user_text += event.unicode

            if active:
                input_cor = cor_bativa

            else:
                input_cor = cor_bpassiva
        #----------jogador escreve o chute
        if draw_input == True:                
            pygame.draw.rect(window,input_cor,input_rect,2)
            superfice_texto = fonte_base.render(user_text,True,input_cor)
            window.blit(superfice_texto,(input_rect.x + 5, input_rect.y + 5))
            
        #----------tentativas na tela:
        window.blit(texto, (700,50))        

        #----------função que atualiza a tela
        pygame.display.update()        
        pygame.display.flip()

#----------função main
if __name__ == '__main__': 
    main()