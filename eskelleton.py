from cgi import print_form
import pygame
import random
from config import *
from assets import *



def build_snake(self, assets, image):
    self.image = assets[image]
    self.mask = pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect()
    self.speedx = 0
    self.speedy = 0



class BODY(pygame.sprite.Sprite):
    def __init__(self, assets, center, neutro=True):

        pygame.sprite.Sprite.__init__(self)
        build_snake(self=self, assets=assets, image=BODY_IMG)
        self.rect.center = center
        self.neutro = neutro
    
    def update(self):
        pass     

class HEAD(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)
        build_snake(self=self, assets=assets, image=HEAD_IMG)
        self.images = assets[DEAD_IMG]
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2
        self.size = 0
        self.state = 1
        self.index_image = 0
    
    def update(self):
        if self.state == 1:
            self.rect.x += self.speedx  
            self.rect.y += self.speedy

    
        # if self.state == 2:
        #     c = self.rect.center
        #     self.image = self.images[self.index_image]
        #     self.rect = self.image.get_rect()
        #     self.rect.center = c
        #     self.index_image += 1
        #     if self.index_image == len(self.images):
        #         self.state = 9


'''class NEUTRO(pygame.sprite.Sprite):
    def __init__(self, assets, center):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets[HEAD_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0
        self.rect.center = center
    
    def update(self):
        pass        '''




class RAT(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[RAT_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        
        #random.randint(0, WIDTH-RATO_WIDTH)
        #random.randint(0, HEIGHT-RATO_HEIGHT)
        

    def update(self):
        pass

class WALLS(pygame.sprite.Sprite):
    def __init__(self, assets, posx, posy):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['parede']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy
    def update(self):
        pass


class Gameover(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, player, assets):

        pygame.sprite.Sprite.__init__(self)

        self.animacao_morte = assets[DEAD_IMG]
        
        self.frame = 0
        self.image = self.animacao_morte[self.frame] 
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 100
        self.player = player
        

    def update(self):

        agora = pygame.time.get_ticks()

        quantos_ticks_passaram = agora - self.last_update

        if quantos_ticks_passaram > self.frame_ticks:
            
            self.last_update = agora
            self.frame += 1
            if self.frame == len(self.animacao_morte):
                self.player.state = 9
                self.kill()

            else:
                center = self.rect.center
                self.image = self.animacao_morte[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
