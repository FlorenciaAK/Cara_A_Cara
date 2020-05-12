#importações necessárias
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen

# inicio pacote do pygame
pygame.init()

#cria tela com 500 pixels de largura e 400 pixels de altura
pygame.display.set_mode((500,400))

#define o título da janela
pygame.display.set_caption ("Cara a cara")