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
CINZA = (127,127,127)

#----------dimensões da tela
LARGURA = 1400
ALTURA = 750

#----------uniformiza o tamanho dos Botoes 
largura_botao = 90
altura_botao = 150

#----------uniformiza o tamanho do rosto neutro
largura_pn = 400
altura_pn = 300

#----------uniformiza o tamanho das opções para as características
largura_op = 90
altura_op = 90

#----------uniformiza o tamanho dos botões das características a serem escolhidas
largura_carac = 130
altura_carac = 33

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
        self.caracteristicas = [sexo, cor_pele, cor_cabelo, tipo_boca, cor_olho, oculos, pelo_facial, queixo, acessorios]
        


#----------classe que cria os botões das personagens
class Button(pygame.sprite.Sprite):
    def __init__(self,nome_da_imagem, x,y,largura,altura, valor = None,desenha = None):
        #----------Define o botão importando as sprites das personagens
        self.arquivo = os.path.join("assets","img",nome_da_imagem)
        self.image = carrega_imagens(self.arquivo)
        self.image = pygame.transform.scale(self.image,(largura,altura)) 
        #----------ponto superior esquerdo da imagem
        self.x = x
        self.y = y
        #----------define altura e largura dos botoes para a funcao draw
        self.largura = largura
        self.altura = altura
        #----------variável que adiciona ou retira o x em cima da personagem
        self.selecionada = False
        self.valor = valor
        self.desenha = desenha
        

    #----------função que desenha o botao na tela 
    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.largura+4,self.altura+4),0)
            
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
    def __init__(self, color, x, y, width, height, text, tam_fonte, valor = None,desenha = None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.tamanho_da_fonte = tam_fonte
        self.valor = valor
        self.desenha = desenha
        self.lista = []
    

    def draw(self, win, outline=None, tam_fonte=20):
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

    #----------criação dicionario
    personagens_dic = {}

    #----------criação dos objetos tipo Carac (personagens)
    Rodrigo = Carac('masculino',   'clara',  'castanho', 'fechada', 'castanhos', 'nao',   'nao',    'pontudo',  'nao')
    Karina = Carac('feminino',     'escura', 'castanho', 'aberta',  'verdes',    'nao',   'nao',    'redondo',  'brincos')
    Ricardo = Carac('masculino',   'clara',  'preto',    'aberta',  'castanhos', 'nao',   'barba',  'redondo',  'nao')
    Bruno = Carac('masculino',     'clara',  'loiro',    'fechada', 'verdes',    'sim',   'barba',  'redondo',  'nao')
    Paula = Carac('feminino',      'clara',  'loiro',    'fechada', 'castanhos ','nao',   'nao',    'redondo',  'batom')
    Francisco = Carac('masculino', 'clara',  'castanho', 'aberta',  'azuis',     'nao',   'bigode', 'pontudo',  'nao')
    Erica = Carac('feminino',      'clara',  'loiro',    'fecada',  'azuis',     'sim',   'nao',    'redondo',  'chapeu')
    Sonia = Carac('feminino',      'clara',  'branco',   'fechada', 'verdes',    'sim',   'nao',    'pontudo',  'brincos')
    Felipe = Carac('masculino',    'clara',  'nao',      'aberta',  'pretos',   'sim',    'bigode', 'pontudo',  'nao')
    Julia = Carac('feminino',      'clara',  'castanho', 'fechada', 'pretos',    'nao',   'nao',    'redondo',  'nao')
    Eduardo = Carac('masculino' ,  'clara',  'loiro',    'aberta',  'azuis',     'nao',   'nao',    'pontudo',  'chapeu')
    Mariana = Carac('feminino',    'clara',  'branco',   'fechada', 'castanhos', 'nao',   'nao',    'redondo',  'brincos')
    Pedro = Carac('masculino',    'clara',   'preto',    'fechada', 'verdes',    'nao',   'nao',    'redondo',  'chapeu')
    Gisele = Carac('feminino',    'escura',  'preto',    'fechada', 'castanhos', 'nao',   'nao',    'redondo',  'brincos')
    Juliana = Carac('feminino',   'clara',   'preto',    'aberta',  'pretos',    'nao',   'nao',    'redondo',  'brincos')
    Robson = Carac('masculino',   'escura',  'preto',    'fechada', 'castanho',  'sim',   'nao',    'redondo',  'nao')
    Aline = Carac('feminino',     'clara',   'ruivo',    'aberta',  'verdes',    'sim',   'nao',    'pontudo',  'nao')
    Gabriel = Carac('masculino',  'escura',  'preto',    'aberta',  'castanhos', 'nao',   'nao',    'pontudo',  'faixa')
    Nathalia = Carac('feminino',  'escura',  'preto',    'fechada', 'castanhos', 'nao',   'nao',    'pontudo',  'brincos')
    Daniel = Carac('masculino',   'clara',   'ruivo',    'aberta',  'castanhos', 'nao',   'barba',  'redondo',  'nao')
    Marcelo = Carac('masculino',  'clara',   'nao',      'aberta',  'pretos',    'nao',   'barba',  'redondo',  'nao')
    Joao = Carac('masculino',     'clara',   'branco',   'fechada', 'pretos',    'nao',    'nao',   'pontudo',  'chapeu')
    Marta = Carac('feminino',     'clara',   'preto',    'aberta',  'azuis',     'nao',    'nao',   'redondo',  'brincos')
    Renato = Carac('masculino',   'clara',   'preto',    'fechada', 'pretos',    'nao',    'nao',   'redondo',  'nao')

    #----------criação dos objetos do tipo button, que define um botao para cada uma das personagens
    Aline_button = Button('Aline.jpg',10,20,largura_botao,altura_botao)
    Rodrigo_button = Button('Rodrigo.jpg',10,206,largura_botao,altura_botao)
    Karina_button = Button('Karina.jpg',10,392,largura_botao,altura_botao)
    Ricardo_button = Button('Ricardo.jpg',10,578,largura_botao,altura_botao)
    Bruno_button = Button('Bruno.jpg',110,20,largura_botao,altura_botao)
    Paula_button = Button('Paula.jpg',110,206,largura_botao,altura_botao)
    Francisco_button = Button('Francisco.jpg',110,392,largura_botao,altura_botao)
    Erica_button = Button('Erica.jpg',110,578,largura_botao,altura_botao)
    Sonia_button = Button('Sonia.jpg',210,20,largura_botao,altura_botao)
    Felipe_button = Button('Felipe.jpg',210,206,largura_botao,altura_botao)
    Julia_button = Button('Julia.jpg',210,392,largura_botao,altura_botao)
    Eduardo_button = Button('Eduardo.jpg',210,578,largura_botao,altura_botao)
    Mariana_button = Button('Mariana.jpg',310,20,largura_botao,altura_botao)
    Pedro_button = Button('Pedro.jpg',310,206,largura_botao,altura_botao)
    Gisele_button = Button('Gisele.jpg',310,392,largura_botao,altura_botao)
    Juliana_button = Button('Juliana.jpg',310,578,largura_botao,altura_botao)
    Robson_button = Button('Robson.jpg',410,20,largura_botao,altura_botao)
    Gabriel_button = Button('Gabriel.jpg',410,206,largura_botao,altura_botao)
    Nathalia_button = Button('Nathalia.jpg',410,392,largura_botao,altura_botao)
    Daniel_button = Button('Daniel.jpg',410,578,largura_botao,altura_botao)
    Marcelo_button = Button('Marcelo.jpg',510,20,largura_botao,altura_botao)
    Joao_button = Button('Joao.jpg',510,206,largura_botao,altura_botao)
    Marta_button = Button('Marta.jpg',510,392,largura_botao,altura_botao)
    Renato_button = Button('Renato.jpg',510,578,largura_botao,altura_botao)

    #----------dicionário que contem as características das personagens
    personagens_dic["Rodrigo"]={"Button":Rodrigo_button,"Caracteristicas":Rodrigo}
    personagens_dic["Karina"]={"Button":Karina_button,"Caracteristicas":Karina}
    personagens_dic["Ricardo"]={"Button":Ricardo_button,"Caracteristicas":Ricardo}
    personagens_dic["Bruno"]={"Button":Bruno_button,"Caracteristicas":Bruno}
    personagens_dic["Paula"]={"Button":Paula_button,"Caracteristicas":Paula}
    personagens_dic["Francisco"]={"Button":Francisco_button,"Caracteristicas":Francisco}
    personagens_dic["Erica"]={"Button":Erica_button,"Caracteristicas":Erica}
    personagens_dic["Sonia"]={"Button":Sonia_button,"Caracteristicas":Sonia}
    personagens_dic["Felipe"]={"Button":Felipe_button,"Caracteristicas":Felipe}
    personagens_dic["Julia"]={"Button":Julia_button,"Caracteristicas":Julia}
    personagens_dic["Eduardo"]={"Button":Eduardo_button,"Caracteristicas":Eduardo}
    personagens_dic["Mariana"]={"Button":Mariana_button,"Caracteristicas":Mariana}
    personagens_dic["Pedro"]={"Button":Pedro_button,"Caracteristicas":Pedro}
    personagens_dic["Gisele"]={"Button":Gisele_button,"Caracteristicas":Gisele}
    personagens_dic["Juliana"]={"Button":Juliana_button,"Caracteristicas":Juliana}
    personagens_dic["Robson"]={"Button":Robson_button,"Caracteristicas":Robson}
    personagens_dic["Aline"]={"Button":Aline_button,"Caracteristicas":Aline}
    personagens_dic["Gabriel"]={"Button":Gabriel_button,"Caracteristicas":Gabriel}
    personagens_dic["Nathalia"]={"Button":Nathalia_button,"Caracteristicas":Nathalia}
    personagens_dic["Daniel"]={"Button":Daniel_button,"Caracteristicas":Daniel}
    personagens_dic["Marcelo"]={"Button":Marcelo_button,"Caracteristicas":Marcelo}
    personagens_dic["Joao"]={"Button":Joao_button,"Caracteristicas":Joao}
    personagens_dic["Marta"]={"Button":Marta_button,"Caracteristicas":Marta}
    personagens_dic["Renato"]={"Button":Renato_button,"Caracteristicas":Renato}

    
    #----------criação dos objetos do tipo settings
    Regras = Settings(VERMELHO, 150 , 300, 400, 200,'Regras',60) 
    Inicio = Settings(VERDE, 850 , 300, 400, 200,'Iniciar',60)
    Chutar = Settings(AZUL,1000,20,200,100,'Chutar', 60)
    Sim = Settings(VERDE,850,250,100,50,'Sim',35, 'sim')
    Nao = Settings(VERMELHO,1050,250,100,50,'Não',35, 'nao')
    Errou = Settings(VERMELHO, 850, 200, 400, 40, 'Chute errado, continue jogando', 30)
    Tem_sim = Settings(VERDE,950,250,150,50,'Acertou',35, 'sim')
    Tem_nao = Settings(VERMELHO,950,250,150,50,'Errou',35, 'nao') 

    #----------criação dos objetos do tipo setting, que define um botao para cada uma das características
    sexo_button = Settings(CINZA, 950, 680, largura_carac, altura_carac,'Sexo', 20)
    pele_button = Settings(CINZA, 1190, 390, largura_carac, altura_carac,'Cor da pele', 20)
    cabelo_button = Settings(CINZA, 680, 390, largura_carac, altura_carac,'Cor do cabelo', 20)
    boca_button = Settings(CINZA, 1190, 567, largura_carac, altura_carac,'Tipo de boca', 20)
    olho_button = Settings(CINZA, 680, 480, largura_carac, altura_carac,'Cor do olho', 20)
    oculos_button = Settings(CINZA, 1190, 485, largura_carac, altura_carac,'Óculos', 20)
    barba_button = Settings(CINZA, 680, 570, largura_carac, altura_carac,'Pelo facial', 20)
    queixo_button = Settings(CINZA, 1190, 617, largura_carac, altura_carac,'Tipo de queixo', 20)
    acessorios_button = Settings(CINZA, 680, 527, largura_carac, altura_carac,'Acessórios', 20)

    #----------criação dos objetos da característica sexo
    masculino_button = Button('sexo_masculino.jpeg', 850, 200,largura_op,altura_op, 'masculino',False)
    feminino_button = Button('sexo_feminino.jpeg', 1050, 200,largura_op,altura_op, 'feminino',False)
    
    #----------criação dos objetos da característica pele
    clara_button = Button('pele_clara.jpeg', 850, 200,largura_op,altura_op, 'clara',False)
    escura_button = Button('pele_escura.jpeg', 1050, 200,largura_op,altura_op, 'escura',False)

    #----------criação dos objetos da característica cabelo
    cabelo_preto_button = Button('cabelo_preto.jpeg', 700, 200,largura_op,altura_op, 'preto',False)
    cabelo_branco_button = Button('cabelo_branco.jpeg', 800, 200,largura_op,altura_op, 'branco',False)
    cabelo_loiro_button = Button('cabelo_loiro.jpeg', 900, 200,largura_op,altura_op, 'loiro',False)
    cabelo_ruivo_button = Button('cabelo_ruivo.jpeg', 1000, 200,largura_op,altura_op, 'ruivo',False)
    cabelo_castanho_button = Button('cabelo_castanho.jpeg',1100, 200,largura_op,altura_op, 'castanho',False)
    careca_button = Button('careca.png',1200, 200,largura_op,altura_op, 'nao',False)

    #----------criação dos objetos da característica boca
    boca_aberta_button = Button('boca_aberta.jpeg', 850, 200,largura_op,altura_op, 'aberta',False)
    boca_fechada_button = Button('boca_fechada.jpeg', 1050, 200,largura_op,altura_op, 'fechada',False)

    #----------criação dos objetos da característica olhos
    olho_preto_button = Button('olhos_pretos.jpeg', 800, 200,largura_op,altura_op, 'pretos',False)
    olho_azul_button = Button('olhos_azuis.jpeg', 900, 200,largura_op,altura_op, 'azuis',False)
    olho_verde_button = Button('olhos_verdes.jpeg', 1000, 200,largura_op,altura_op, 'verdes',False)
    olho_castanho_button = Button('olhos_castanhos.jpeg',1100, 200,largura_op,altura_op, 'castanhos',False)

    #----------criação dos objetos da característica óculos
    com_oculos_button = Button("com_oculos.png",850,200,largura_op,altura_op, 'sim',False)
    sem_oculos_button = Button("sem_oculos.png",1050,200,largura_op,altura_op, 'nao',False)

    #----------criação dos objetos da característica pelo facial
    pelo_facial_barba_button = Button('barba.jpeg', 850, 200,largura_op,altura_op, 'barba',False)
    pelo_facial_bigode_button = Button('bigode.jpeg', 950, 200,largura_op,altura_op, 'bigode',False)
    nao_pelo_facial_button = Button('sem_pelo.jpeg',1050,200,largura_op,altura_op,'nao',False)

    #----------criação dos objetos da característica queixo
    queixo_redondo_button = Button('queixo_redondo.jpeg', 850, 200,largura_op,altura_op, 'redondo',False)
    queixo_pontudo_button = Button('queixo_pontudo.jpeg', 1050, 200,largura_op,altura_op, 'pontudo',False)

    #----------criação dos objetos da característica acessórios
    batom_button = Button('batom.jpeg', 750, 200,largura_op,altura_op, 'batom', False)
    faixa_button = Button('faixa.jpeg', 850, 200,largura_op,altura_op, 'faixa', False)
    chapeu_button = Button('chapeu.jpeg', 950, 200,largura_op,altura_op, 'chapeu', False)
    brinco_button = Button('brinco.jpeg',1050, 200,largura_op,altura_op, 'brincos', False)
    sem_acessorios_button = Button('sem_acessorios.jpeg',1150,200,largura_op,altura_op, 'nao', False)

    sexo_button.lista = [masculino_button,feminino_button]
    pele_button.lista = [clara_button,escura_button]
    cabelo_button.lista = [cabelo_preto_button,cabelo_branco_button,cabelo_castanho_button,cabelo_loiro_button,cabelo_ruivo_button,careca_button]
    boca_button.lista = [boca_aberta_button,boca_fechada_button]
    olho_button.lista = [olho_preto_button,olho_azul_button,olho_castanho_button,olho_verde_button]
    oculos_button.lista = [com_oculos_button,sem_oculos_button]
    barba_button.lista = [pelo_facial_barba_button,pelo_facial_bigode_button, nao_pelo_facial_button]
    queixo_button.lista = [queixo_pontudo_button,queixo_redondo_button]
    acessorios_button.lista = [batom_button,faixa_button,chapeu_button,brinco_button,sem_acessorios_button]

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
    nomes_personagens = ["Rodrigo", "Karina", "Ricardo", "Bruno", "Paula", "Francisco", "Erica", "Sonia", "Felipe", "Julia", "Eduardo", "Mariana", "Pedro", "Gisele", "Juliana", "Robson","Aline", "Gabriel", "Nathalia", "Daniel", "Marcelo", "Joao", "Marta", "Renato"] 
    #----------personagens sorteados
    personagem_sorteio_i = random.randrange(0,len(nomes_personagens))
    personagem_escolhido = nomes_personagens [personagem_sorteio_i]
    personagem_escolhido_lower = personagem_escolhido.lower()

    for k in personagens_dic:
        if personagem_escolhido == personagens_dic[k]:
            num = k
    print(personagem_escolhido)

    #----------variável que define quando o jogo acaba
    game = False
    desenha_temsim = False
    desenha_temnao = False
    desenha_errou = False
    dt_temsim = pygame.time.get_ticks()
    dt_temnao = pygame.time.get_ticks()
    dt_errou = pygame.time.get_ticks()

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
    contador_c = 3
    contador_p = 10

    #----------variável que determina se as regras estão sendo mostradas
    manual = False

    #----------começa a interção com o jogador----------
    #----------verifica se o jogador clicou em algum botão e direciona para tela especifica
    while not game:
        #----------Marca um ritmo pro computador funcionar
        clock.tick(FPS)

        #----------devolve uma lista com os acontecimentos do teclado e mouse
        eventos = pygame.event.get()

        #----------variavel da posição do mouse
        pos = pygame.mouse.get_pos()

        #----------percorre a lista de eventos
        for evento in eventos:
            #----------verifica se o jogador clicou no x vermelho da tela
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
                game = False
                pygame.quit()              
                sys.exit() 

            #----------verifica se o mouse está sobre o botão iniciar e se este foi clicado
            if evento.type == pygame.MOUSEBUTTONDOWN and Inicio.isOver(pos):
                game = True
                break
        
            #----------verifica se o mouse está sobre o botão regras e se este foi clicado
            if evento.type == pygame.MOUSEBUTTONDOWN and Regras.isOver(pos):
                #----------Marca um ritmo pro computador funcionar
                clock.tick(FPS)
                #----------desenha as regras na tela
                window.blit(regras, (0,0))
                pygame.display.flip()
                manual = True
                #----------verifica se o jogador clicou em qualquer tecla para iniciar o jogo 
            if manual and (evento.type == pygame.KEYDOWN):
                game = True
                break

    while game:
        #----------Marca um ritmo pro computador funcionar
        clock.tick(FPS)
        
        #----------preenche tela com cor branca
        window.fill(BRANCO)

        #----------coloca a quantidade de chutes restantes na tela:
        font = pygame.font.SysFont("TimesNewRoman", 30)
        chutes = font.render("Chutes restantes: {0}".format(contador_c), True, PRETO)
        perguntas = font.render("Perguntas restantes: {0}".format(contador_p), True, PRETO)

        #----------Desenha os rosto neutro
        window.blit(pessoa_neutra,(800,350))

        #----------Desenha os botões das personagens 
        personagens_botoes = [Aline_button,Rodrigo_button,Karina_button,Ricardo_button,Bruno_button,Paula_button,Francisco_button,Erica_button,Sonia_button,Felipe_button,Julia_button,Eduardo_button,Mariana_button,Pedro_button,Gisele_button,Juliana_button,Robson_button,Gabriel_button,Nathalia_button,Daniel_button,Marcelo_button,Joao_button,Marta_button,Renato_button]
        for p in personagens_botoes:
            p.draw(window,PRETO)

        #----------Desenha os botão chutar
        Chutar.draw(window,PRETO)

        #----------Desenha os botões das características
        carac_botoes = [sexo_button,pele_button,cabelo_button,boca_button,olho_button,oculos_button,barba_button,queixo_button,acessorios_button]
        
        for f in carac_botoes:
            f.draw(window,PRETO)

        #----------variável da posição do mouse
        pos = pygame.mouse.get_pos()

        #----------coleta de eventos
        eventos = pygame.event.get()

        #----------varíavel que determina se foi feita uma pergunta
        apertou = False

        perdeu = False

        #----------percorre a lista de eventos
        for event in eventos:
            #----------evento para sair do jogo
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                game = False
                pygame.quit()              
                sys.exit() 

            #----------evento que verifica se o botão do mouse foi clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in personagens_botoes:
                    if b.isOver(pos):
                        if b.selecionada == False:
                            b.selecionada = True
                        elif b.selecionada == True:
                            b.selecionada = False
                        som_x.play()
                #----------evento que verifica se o jogador clicou no botão chute
                if Chutar.isOver(pos):
                    draw_input = True
                #----------evento para checar a seleção do input do chute
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                #----------evento que verifica se o jogador clicou em alguma das características
                #----------checa as carac gerais e desenha as específicas
                for carac_geral in carac_botoes:
                    if carac_geral.isOver(pos):
                        if carac_geral.desenha == False:
                           carac_geral.desenha = True
                        else:
                            carac_geral.desenha = False
                    if carac_geral.desenha:
                        for carac_esp in carac_geral.lista:
                            if carac_esp.isOver(pos):
                                if carac_esp.valor in personagens_dic[personagem_escolhido]['Caracteristicas'].caracteristicas:
                                    apertou = True
                                    carac_geral.desenha = False
                                    desenha_temsim = True
                                    dt_temsim = pygame.time.get_ticks()
                                elif carac_esp.valor not in personagens_dic[personagem_escolhido]['Caracteristicas'].caracteristicas:
                                    apertou = True
                                    desenha_temnao = True
                                    carac_geral.desenha = False
                                    dt_temnao = pygame.time.get_ticks()

            #----------evento que permite realizar o chute
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        user_text_lower = user_text.lower()
                        if user_text_lower == personagem_escolhido_lower:
                            #----------tela do vencedor
                            venceu_dir = os.path.join("assets","img",'Tela_ganhadora.jpeg')  
                            venceu_load = carrega_imagens(venceu_dir)
                            venceu = pygame.transform.scale(venceu_load, (LARGURA, ALTURA))
                            window.blit(venceu, (0, 0))
                            pygame.display.update()
                            pygame.time.delay(5000)
                            game = False
                        else:
                            contador_c -= 1
                            if contador_c>0:
                                desenha_errou = True
                                dt_errou = pygame.time.get_ticks()
                            if contador_c == 0:
                                perdeu = True
                                
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
        if sexo_button.desenha == True:
            masculino_button.draw(window,PRETO)
            feminino_button.draw(window,PRETO)
        if pele_button.desenha == True:
            clara_button.draw(window,PRETO)
            escura_button.draw(window,PRETO)
        if cabelo_button.desenha == True:
            cabelo_branco_button.draw(window,PRETO)
            cabelo_castanho_button.draw(window,PRETO)
            cabelo_loiro_button.draw(window,PRETO)
            cabelo_preto_button.draw(window,PRETO)
            cabelo_ruivo_button.draw(window,PRETO)
            careca_button.draw(window,PRETO)
        if boca_button.desenha == True:
            boca_aberta_button.draw(window,PRETO)
            boca_fechada_button.draw(window,PRETO)
        if olho_button.desenha == True:
            olho_castanho_button.draw(window,PRETO)
            olho_azul_button.draw(window,PRETO)
            olho_preto_button.draw(window,PRETO)
            olho_verde_button.draw(window,PRETO)
        if oculos_button.desenha == True:
            com_oculos_button.draw(window,PRETO)
            sem_oculos_button.draw(window,PRETO)
        if barba_button.desenha == True:
            pelo_facial_bigode_button.draw(window,PRETO)
            pelo_facial_barba_button.draw(window,PRETO)
            nao_pelo_facial_button.draw(window,PRETO)
        if queixo_button.desenha == True:
            queixo_pontudo_button.draw(window,PRETO)
            queixo_redondo_button.draw(window,PRETO)
        if acessorios_button.desenha == True:
            batom_button.draw(window,PRETO)
            brinco_button.draw(window,PRETO)
            faixa_button.draw(window,PRETO)
            chapeu_button.draw(window,PRETO)
            sem_acessorios_button.draw(window,PRETO)

        now = pygame.time.get_ticks()

        if desenha_temsim:
            Tem_sim.draw(window, PRETO)
            if now - dt_temsim > 2000:
                desenha_temsim = False 
            
        if desenha_temnao:
            Tem_nao.draw(window, PRETO)
            if now - dt_temnao > 2000:
                desenha_temnao = False 

        if desenha_errou:
            Errou.draw(window, PRETO)
            if now - dt_errou > 2000:
                desenha_errou = False

        if apertou:
            contador_p -=1

        if contador_p < 0:
            perdeu = True

        if perdeu:
            perdeu_dir = os.path.join("assets","img",'Tela_perdedora.jpeg')  
            perdeu_load = carrega_imagens(perdeu_dir)
            perdeu = pygame.transform.scale(perdeu_load, (LARGURA, ALTURA))
            window.blit(perdeu, (0, 0))
            pygame.display.update()
            pygame.time.delay(5000)
            game = False
        
        #----------tentativas na tela:
        window.blit(chutes, (700,50))
        window.blit(perguntas, (700,100))  


        #----------função que atualiza a tela
        pygame.display.update()        
        pygame.display.flip()

#----------função main
if __name__ == '__main__': 
    main()