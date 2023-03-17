import pygame
from config import *
from assets import *
from eskelleton import *
import time

def le_mapa():
    with open(f'assets/labirintos/labirinto2.csv', 'r') as arquivo:
        fase_lines = arquivo.readlines()
    return fase_lines

def cria_labirinto(assets, mapa, all_sprites):    
    all_walls = pygame.sprite.Group()
    for l in range(len(mapa)):
        for c in range(len(mapa[l])):
            e = mapa[l][c]
            if e == '1':
                w = WALLS(assets, c*SIZE, l*SIZE)
                all_walls.add(w)
                all_sprites.add(w)
    return all_walls

def pagina_jogo(WINDOW):
#SPRITES
    state = GAME
    assets = carrega_assets()

    all_sprites = pygame.sprite.Group()
    player = HEAD(assets)
    all_sprites.add(player)
    #body = pygame.sprite.Group()
    all_rats = pygame.sprite.Group()
    maze_walls = pygame.sprite.Group()
    all_bodies = pygame.sprite.Group()
    
    font = pygame.font.Font(None, 60)

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_bodies'] = all_sprites
    groups['all_rats'] = all_rats
    groups['maze_walls'] = maze_walls
    groups['all_neutros'] = all_sprites

    mapa = le_mapa()    
    all_walls = cria_labirinto(assets, mapa, all_sprites)

    elemento = '1'
    while elemento != "9":
        l = random.randint(0, len(mapa) - 1)
        c = random.randint(0, len(mapa[l]) - 1)
        elemento = mapa[l][c]
    rat = RAT(assets, c*SIZE, l*SIZE)
    all_sprites.add(rat)
    all_rats.add(rat)


    clock = pygame.time.Clock()
    VEL = 3
    NIVEL = 1
    score = 0 
    placar = 0
    count = 1


    #assets[BATIDA_SOUND].play(loops=-1)
    pygame.mixer.music.set_volume(0.4)

    game = True
    while game:
        se_comeu = 'n'
        if placar >= score:
            placar = score
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    state = QUIT
                    game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    state = QUIT
                    game = False
                if event.key == pygame.K_LEFT and player.speedx != VEL and player.speedx != -VEL:     #left
                    player.speedx -= VEL     
                    player.speedy = 0       
                if event.key == pygame.K_RIGHT and player.speedx != -VEL and player.speedx != VEL:    #right
                    player.speedx += VEL
                    player.speedy = 0   
                if event.key == pygame.K_UP and player.speedy != VEL and player.speedy != -VEL:       #up
                    player.speedy -= VEL
                    player.speedx = 0   
                if event.key == pygame.K_DOWN and player.speedy != -VEL and player.speedy != VEL:     #down
                    player.speedy += VEL
                    player.speedx = 0   


        # if player.rect.x < 0 or player.rect.x > (WIDTH - COBRA_WIDTH) or player.rect.y < 0 or player.rect.y > (HEIGHT - COBRA_HEIGHT):
        #   
        #     exp = Gameover(player.rect.center, assets)
        #     all_sprites.add(exp)
        #     game = False
        #     state = GAMEOVER
            
        
        c = player.rect.center
        all_sprites.update()  
        
        if len(all_bodies) < player.size:
            b = BODY(assets, c)
            all_sprites.add(b)
            all_bodies.add(b)
        elif len(all_bodies) == 0:
            pass
        else:
            all_bodies.sprites()[0].kill()
        for i in range(len(all_bodies)-15):
            all_bodies.sprites()[i].neutro = False


        papa_rato = pygame.sprite.spritecollide(player, all_rats, True, pygame.sprite.collide_mask)
        if len(papa_rato) > 0:
            assets[NHAC_SOUND].play()
            for rato in papa_rato:
                elemento = '1'
                while elemento != "9":
                    l = random.randint(0, len(mapa) - 1)
                    c = random.randint(0, len(mapa[l]) - 1)
                    elemento = mapa[l][c]
                r = RAT(assets, c*SIZE, l*SIZE)
                all_sprites.add(r)
                all_rats.add(r)

                player.size += 7
                score += 1

                if score%10 == 0:
                    VEL += 0.0
                    NIVEL += 1
                
                    
        se_comeu = pygame.sprite.spritecollide(player, all_bodies, False, pygame.sprite.collide_mask)
        for body in se_comeu:
            if not body.neutro and count == 1:
                se_comeu = 's'
                count += 1

        if se_comeu == 's' and player.state == 1:
            player.state = 2
            exp = Gameover(CENTER, player, assets)
            all_sprites.add(exp)
            #assets[BATIDA_SOUND].stop()
            assets[DIE_SOUND].play()


                
                
        bateu_parede = pygame.sprite.spritecollide(player, all_walls, False, pygame.sprite.collide_mask)
        if player.state == 1 and len(bateu_parede) > 0:
            player.state = 2
            exp = Gameover(CENTER, player, assets)
            all_sprites.add(exp)
            #assets[BATIDA_SOUND].stop()
            assets[DIE_SOUND].play()
            
        
        if player.state == 9:
            state = GAMEOVER
            game = False

        #vou tentar implementar o recorde
        
        WINDOW.fill(BLUE)  # Preenche com a cor azul

        all_sprites.draw(WINDOW)

        text_surface = assets[SCORE_FONTE].render("RATOS PAPADOS:  {} ".format(score), True, (BLACK))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  0)
        WINDOW.blit(text_surface, text_rect)

        text_level = assets[SCORE_FONTE].render("NIVEL:  {} ".format(NIVEL), True, (BLACK))
        text_rect = text_level.get_rect()
        text_rect.midtop = (60,  0)
        WINDOW.blit(text_level, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
        
    
    return state