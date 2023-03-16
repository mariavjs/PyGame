import pygame
import os
from os import path
from config import *
#os.chdir(os.path.dirname(os.path.abspath(_file_)))

#IMG_DIR = path.join(path.dirname(_file_), 'assets', 'imagens')
#SND_DIR = path.join(path.dirname(_file_), 'assets', 'sons')
#FNT_DIR = path.join(path.dirname(_file_), 'assets', 'font') 

#imagens
HEAD_IMG = 'cabeca'
NEUTRO_IMG = 'neutro'
BODY_IMG = 'body'
RAT_IMG = 'rato'
WALL_IMG = 'parede'
DEAD_IMG = 'cobra_morta'
PAG_INICIAL = 'pag_inicial'
PAG_GAMEOVER = 'pag_gameover'

#sons
NHAC_SOUND = 'eat_sound'
EW_SOUND = 'throwingup_sound'
BATIDA_SOUND = 'batida_sound'
DIE_SOUND = 'die_sound'

#fontes
SCORE_FONTE = 'score_fonte'
GAMEOVER_FONTE = 'gameover_fonte'
TELAINICIAL_FONTE = 'telainicial_fonte'


def carrega_assets():
    assets = {}
    #assets[CENARIO] = pygame.image.load(os.path.join(IMG_DIR, 'cenario.png')).convert()
    assets[HEAD_IMG] = pygame.image.load('assets/imagens/verde.png').convert_alpha()
    assets[HEAD_IMG] = pygame.transform.scale(assets[HEAD_IMG], (COBRA_WIDTH, COBRA_HEIGHT))
    assets[NEUTRO_IMG] = pygame.image.load('assets/imagens/verde.png').convert_alpha()
    assets[NEUTRO_IMG] = pygame.transform.scale(assets[HEAD_IMG], (COBRA_WIDTH, COBRA_HEIGHT))
    assets[BODY_IMG] = pygame.image.load('assets/imagens/verde.png').convert_alpha()
    assets[BODY_IMG] = pygame.transform.scale(assets[BODY_IMG], (COBRA_WIDTH, COBRA_HEIGHT))
    #assets[DEAD_IMG] = pygame.image.load('assets/imagens/cobramortapng.png').convert_alpha()
    #assets[DEAD_IMG] = pygame.transform.scale(assets[DEAD_IMG], (300, 300))
    assets[RAT_IMG] = pygame.image.load('assets/imagens/rato.png').convert_alpha()
    assets[RAT_IMG] = pygame.transform.scale(assets[RAT_IMG], (RATO_WIDTH, RATO_HEIGHT))
    assets[WALL_IMG] = pygame.image.load('assets/imagens/parede.png').convert_alpha()
    assets[WALL_IMG] = pygame.transform.scale(assets[WALL_IMG], (SIZE, SIZE))
    assets[PAG_GAMEOVER] = pygame.image.load('assets/imagens/finalll.png').convert_alpha()
    assets[PAG_GAMEOVER] = pygame.transform.scale(assets[PAG_GAMEOVER], (WIDTH, HEIGHT))
    assets[PAG_INICIAL] = pygame.image.load('assets/imagens/inicialll.png').convert_alpha()
    assets[PAG_INICIAL] = pygame.transform.scale(assets[PAG_INICIAL], (WIDTH, HEIGHT))


    lista_animacao = []
    for imagem in range(1, 9):
        filename = pygame.image.load('assets/imagens/cobrabateu0.png').convert_alpha()

        img = pygame.transform.scale(filename, (imagem*70, imagem*70))
        lista_animacao.append(img)
    
    assets[DEAD_IMG] = lista_animacao
    
    # Carrega os sons do jogo
    #pygame.mixer.music.load('assets/sons/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    #pygame.mixer.music.set_volume(0.4)
    assets[NHAC_SOUND] = pygame.mixer.Sound('assets/sons/cobracomendocurto.wav')
    #assets[EW_SOUND] = pygame.mixer.Sound('assets/snd/expl6.wav')
    #assets[BATIDA_SOUND] = pygame.mixer.Sound('assets/sons/gostosinho.wav')
    assets[DIE_SOUND] = pygame.mixer.Sound('assets/sons/som_gameoveroficial.wav')

    #carrega as fontes do jogo
    assets[SCORE_FONTE] = pygame.font.Font(('assets/fontes/fonte_score.ttf'), 28)
    assets[GAMEOVER_FONTE] = pygame.font.Font(('assets/fontes/fonte_gameover.ttf'), 28)
    assets[TELAINICIAL_FONTE] = pygame.font.Font(('assets/fontes/fonte_telainicial.ttf'), 28)

    
    return assets