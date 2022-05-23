import pygame

pygame.init()

#especificacoes tela
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PAPA RATOS')

#cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (107, 142, 35)
BROWN = (139, 0, 0)

#texto
font = pygame.font.SysFont(None, 48)
text = font.render('COMECAR(ENTER)', True, (0, 0, 255))
text2 = font.render('SAIR(S)', True, (0, 0, 255))

#dimencoes bordas
BORDER_DIAMETER = 30
BORDER_LEFT = pygame.Rect(0, 0, BORDER_DIAMETER, HEIGHT)
BORDER_RIGHT = pygame.Rect(WIDTH - BORDER_DIAMETER, 0, BORDER_DIAMETER, HEIGHT)
BORDER_UP = pygame.Rect(0, 0, WIDTH, BORDER_DIAMETER)
BORDER_DOWN = pygame.Rect(0, HEIGHT - BORDER_DIAMETER, WIDTH, BORDER_DIAMETER)

#fps e velocidade da cobra
FPS = 30
VEL = 5

#infos cobra
COBRA_WIDTH, COBRA_HEIGHT = 30, 30
COBRA_IMG = pygame.image.load('cobra2.png').convert() #colocar nome da imagem do rato
COBRA_PEQUENO_IMG = pygame.transform.scale(COBRA_IMG, (COBRA_WIDTH, COBRA_HEIGHT))


def draw_window(cobra):
    WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW, BLACK, BORDER_LEFT)
    pygame.draw.rect(WINDOW, BLACK, BORDER_RIGHT)
    pygame.draw.rect(WINDOW, BLACK, BORDER_UP)
    pygame.draw.rect(WINDOW, BLACK, BORDER_DOWN)
    WINDOW.blit(COBRA_PEQUENO_IMG, (cobra.x, cobra.y))
    pygame.display.update()

cobra = pygame.Rect(100, 300, COBRA_WIDTH, COBRA_HEIGHT)

def cobra_handle_movement(keys_pressed,  cobra):
    if keys_pressed[pygame.K_LEFT] and cobra.x - VEL > BORDER_DIAMETER: #left
        cobra.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and cobra.x + VEL < WIDTH - (BORDER_DIAMETER + COBRA_WIDTH): #right
        cobra.x += VEL
    if keys_pressed[pygame.K_UP] and cobra.y - VEL > BORDER_DIAMETER: #up
        cobra.y -= VEL
    if keys_pressed[pygame.K_DOWN] and cobra.y + VEL < HEIGHT - (BORDER_DIAMETER + COBRA_HEIGHT): #down
        cobra.y += VEL

clock = pygame.time.Clock()

class cobra(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cor = 'verde'

def tela_inicial():
    game = True
    while game:
        WINDOW.fill(GREEN)
        WINDOW.blit(text, (10, 10))
    pygame.quit()


def pagina_jogo():
    game = True
    while game:    
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()
        cobra_handle_movement(keys_pressed, cobra)
        draw_window(cobra)
        
    pygame.quit()

tela_inicial()