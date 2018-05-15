import pygame
from Windows import windows,functions,cut
from enemies.enemy import *
from  bullets.bullet import *
from players.player import *
from Items.item import item
import ConfigParser
import random
r=lambda: random.randint(0,255)
rx=lambda: random.randint(0,700)
ry=lambda: random.randint(0,400)
robjetive=lambda: random.randint(1,2)

SIZE_SCREEN=[700,500]
VELOCIDAD=5
pygame.init()


# elementos del mapa
class Background (pygame.sprite.Sprite):
    def __init__(self,posx,posy,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
        self.vel_x=0
        self.vel_y=0
    def update (self):
        pass

def main ():
    game_over=False
    win=False
    while not game_over:
        CALACAS=0 # calaveras
        Menu=False
        vidaP1=pygame.font.Font(None,32)
        #screen for gane
        screen=windows.Create_screen(SIZE_SCREEN)
        close=False
        #choose menu
        while not Menu:
            functions.Menu(screen,win)
            windows.show()
            for events in pygame.event.get():
                if events.type==pygame.QUIT:
                    Menu=True
                    game_over=True
                    close=True
                if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_SPACE:
                        Menu=True
                    if events.key==pygame.K_ESCAPE:
                        Menu=True
                        game_over=True
                        close=True
        #read map and info of file extern
        # inter=ConfigParser.ConfigParser()
        # inter.read('Maps/mapa.map')
        #
        # _map=inter.get('nivel','mapa')
        # _Maps=_map.split('\n')
        _Maps=functions.Read_Map('Maps/mapa.map','nivel','mapa')
        img=windows.Create_images('terrenogen.png')
        M1=cut.insert_in_matrix(img,32,12)
        #finish read
        #start images
        img1=windows.Create_images('sprites_characters/Player1.png')
        img2=windows.Create_images('sprites_characters/posiblepersonaje.png')
        img2angel=windows.Create_images('sprites_characters/angelhealer.png')
        img_bullet_haler=windows.Create_images('sprites_characters/spell_basic.png')
        img_e=windows.Create_images('sprites_enemies/adds2.png')
        img_e2=windows.Create_images('sprites_enemies/adds5.png')
        img_Boss=windows.Create_images('sprites_enemies/bossmedium.png')
        img1angel=windows.Create_images('sprites_characters/angeldps.png')
        img_bullet_A=windows.Create_images('sprites_characters/spell.png')
        imgSkill=windows.Create_images('sprites_enemies/SkillMiniboss.png')
        img_adds2=windows.Create_images('sprites_enemies/spellsAdds2.png')
        adds_Mbossimg=windows.Create_images('sprites_enemies/ghost.png')
        img_item=windows.Create_images('Items/calaca.png')
        #finish images
        #Cut images
        m2MBoss=cut.insert_in_matrix(adds_Mbossimg,4,4)
        m1=cut.insert_in_matrix(img1,4,4)
        m2=cut.insert_in_matrix(img2,4,4)
        m2Angel=cut.insert_in_matrix(img2angel,4,4)
        m1Angel=cut.insert_in_matrix(img1angel,4,4)
        e1=cut.insert_in_matrix(img_e,4,4)
        e2=cut.insert_in_matrix(img_e2,4,4)
        boss1=cut.insert_in_matrix(img_Boss,4,4)
        #finish cuting images
        #create objects
        player1=HEALER(m1)
        player2=TANK(m2)
        #finisg objects
        #creating groups
        all_items=pygame.sprite.Group()
        players=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        bullets_enemies2=pygame.sprite.Group()
        all_elements=pygame.sprite.Group()
        Background_elements=pygame.sprite.Group()
        BulletsSpider=pygame.sprite.Group()
        All_Bosses=pygame.sprite.Group()
        walls=pygame.sprite.Group()
        All_enemies2=pygame.sprite.Group()
        All_enemies=pygame.sprite.Group()
        miniAdds=pygame.sprite.Group()
        all_elements.add(player1)
        all_elements.add(player2)
        players.add(player1)
        players.add(player2)
        clock=pygame.time.Clock()
        pygame.mixer.init()
        SpellHeal=pygame.mixer.Sound('healspell1.ogg')
        SpellDps=pygame.mixer.Sound('spell.wav')
        x=0#incremento de posiciones
        y=0
        #ciclo para la lectura del mapa
        for i in range (len(_Maps)):
            x=0
            for m in _Maps[i]:
                element_X,element_y=functions.Read_section('Maps/mapa.map',m)
                B=Background(x,y,M1[element_y][element_X])
                Background_elements.add(B)
                x+=32
                if m=='O':
                    i=item(img_item,x,y)
                    all_elements.add(i)
                    all_items.add(i)
                    Background_elements.add(i)
                if m=='#': # paredes
                    walls.add(B)
                if m=='C': #enemigos de persecusion
                    en=enemies(e1,x,y)
                    all_elements.add(en)
                    All_enemies.add(en)
                    Background_elements.add(en)
                if m=='T':# enemigos que disparan
                    en=enemies2(e2,x,y)
                    all_elements.add(en)
                    All_enemies2.add(en)
                    Background_elements.add(en)
                if m=='X':#miniboss
                    en=Miniboss(boss1,x,y)
                    all_elements.add(en)
                    Background_elements.add(en)
                    All_Bosses.add(en)


            y+=32
        # inicio del juego
        while not close:
            win=False
            for events in pygame.event.get():
                if events.type==pygame.QUIT:
                    close=True
                    game_over=True
            #comportamiento de los jugadores
                if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_UP:
                        player1.UP=True
                    if events.key==pygame.K_DOWN:
                        player1.DOWN=True
                    if events.key==pygame.K_RIGHT:
                        player1.RIGHT=True
                    if events.key==pygame.K_LEFT:
                        player1.LEFT=True
                    if events.key==pygame.K_w:
                        player2.UP=True
                    if events.key==pygame.K_s:
                        player2.DOWN=True
                    if events.key==pygame.K_d:
                        player2.RIGHT=True
                    if events.key==pygame.K_a:
                        player2.LEFT=True
                    if  events.key==pygame.K_x:
                        if player2.coldown ==0:
                            player2.m=m2Angel
                            player2.coldown=300
                            player2.time_angel=150
                            player2.is_angel=True
                    if  events.key==pygame.K_z:
                        player2.m=m2
                    if  events.key==pygame.K_l:
                        if player1.coldown ==0:
                            player1.m=m1Angel
                            player1.coldown=300
                            player1.time_angel=150
                            player1.is_angel=True


                    if events.key==pygame.K_8:
                        player1.is_run=True
                        if player1.time==0:
                            if not player1.is_angel:
                                img_bullet_healer=img_bullet_haler
                            else:
                                img_bullet_healer=img_bullet_A
                            bullet_H=Bullet_player(img_bullet_healer)
                            all_elements.add(bullet_H)
                            bullets.add(bullet_H)
                            bullet_H.rect.x=player1.rect.x
                            bullet_H.rect.y=player1.rect.y
                            if  player1.action==0:
                                bullet_H.vel_y=10
                                bullet_H.vel_x=0
                            if  player1.action==1:
                                bullet_H.vel_x=-10
                                bullet_H.vel_y=0
                            if  player1.action==2:
                                bullet_H.vel_x=10
                                bullet_H.vel_y=0
                            if  player1.action==3:
                                bullet_H.vel_y=-10
                                bullet_H.vel_x=0
                            SpellDps.play()
                    if events.key==pygame.K_9:
                        player1.is_run=True
                        if player1.time==0:
                            if not player1.is_angel:
                                img_bullet_healer=img_bullet_haler
                            else:
                                img_bullet_healer=img_bullet_A
                            bullet_H=Bullet_player(img_bullet_healer)
                            all_elements.add(bullet_H)
                            bullets.add(bullet_H)
                            bullet_H.rect.x=player1.rect.x
                            bullet_H.rect.y=player1.rect.y
                            if  player1.action==0:
                                bullet_H.vel_y=10
                                bullet_H.vel_x=2
                            if  player1.action==1:
                                bullet_H.vel_x=-10
                                bullet_H.vel_y=2
                            if  player1.action==2:
                                bullet_H.vel_x=10
                                bullet_H.vel_y=-2
                            if  player1.action==3:
                                bullet_H.vel_y=-10
                                bullet_H.vel_x=-2
                    if events.key==pygame.K_0:
                        player1.is_run=True
                        if player1.time==0:
                            if not player1.is_angel:
                                img_bullet_healer=img_bullet_haler
                            bullet_H=Bullet_player(img_bullet_healer)
                            all_elements.add(bullet_H)
                            bullets.add(bullet_H)
                            bullet_H.rect.x=player1.rect.x
                            bullet_H.rect.y=player1.rect.y
                            if  player1.action==0:
                                bullet_H.vel_y=10
                                bullet_H.vel_x=-2
                            if  player1.action==1:
                                bullet_H.vel_x=-10
                                bullet_H.vel_y=-2
                            if  player1.action==2:
                                bullet_H.vel_x=10
                                bullet_H.vel_y=2
                            if  player1.action==3:
                                bullet_H.vel_y=-10
                                bullet_H.vel_x=2

                    if events.key==pygame.K_1:
                        if player1.salud < 100:
                            if player2.is_angel:
                                player1.salud+=15
                            else:
                                player1.salud+=5
                            SpellHeal.play()
                            if player1.salud > 100:
                                player1.salud=100
                    if events.key==pygame.K_2:
                        if player2.salud < 80:
                            if player2.is_angel:
                                player2.salud+=15
                            else:
                                player2.salud+=5
                            if player2.salud > 80:
                                player2.salud=80
                            SpellHeal.play()
                    if events.key==pygame.K_3:
                        if player2.salud<80 and player1.salud < 100:
                            if player2.is_angel:
                                player2.salud+=5
                                player1.salud+=5
                            else:
                                player2.salud+=3
                                player1.salud+=3
                            SpellHeal.play()
                if events.type == pygame.KEYUP:
                    if events.key==pygame.K_UP:
                        player1.UP=False
                    if events.key==pygame.K_DOWN:
                        player1.DOWN=False
                    if events.key==pygame.K_RIGHT:
                        player1.RIGHT=False
                    if events.key==pygame.K_LEFT:
                        player1.LEFT=False
                    if events.key==pygame.K_w:
                        player2.UP=False
                    if events.key==pygame.K_s:
                        player2.DOWN=False
                    if events.key==pygame.K_d:
                        player2.RIGHT=False
                    if events.key==pygame.K_a:
                        player2.LEFT=False


    ## start player2







            #comportamiento jugadores
            if player1.time_angel==0:
                player1.m=m1
                player1.is_angel=False
            if player2.time_angel==0:
                player2.m=m2
                player2.is_angel=False

            #colisiones
            #Items
            for p in players:
                col_item=pygame.sprite.spritecollide(p,all_items,True)
                for Col in col_item:
                    CALACAS+=1
            #paredes
            Col_Wall=pygame.sprite.spritecollide(player1,walls,False)
            for col in Col_Wall:
                if player1.vel_x > 0 and  player1.rect.right > col.rect.left:
                    player1.vel_x=0
                    player1.rect.right=col.rect.left
                if player1.vel_x < 0 and player1.rect.left < col.rect.right:
                    player1.vel_x=0
                    player1.rect.left=col.rect.right
                if player1.vel_y > 0 and player1.rect.bottom > col.rect.top:
                    player1.vel_y=0
                    player1.rect.bottom=col.rect.top
                if player1.vel_y < 0 and player1.rect.top < col.rect.bottom:
                    player1.vel_y=0
                    player1.rect.top=col.rect.bottom
            #paredes
            Col_Wall=pygame.sprite.spritecollide(player2,walls,False)
            for col in Col_Wall:
                if player2.vel_x > 0 and  player2.rect.right > col.rect.left:
                    player2.vel_x=0
                    player2.rect.right=col.rect.left
                elif player2.vel_x < 0 and player2.rect.left < col.rect.right:
                    player2.vel_x=0
                    player2.rect.left=col.rect.right
                elif player2.vel_y > 0 and player2.rect.bottom > col.rect.top:
                    player2.vel_y=0
                    player2.rect.bottom=col.rect.top
                elif player2.vel_y < 0 and player2.rect.top < col.rect.bottom:
                    player2.vel_y=0
                    player2.rect.top=col.rect.bottom
            #balas jugador vs enemigos
            for e in All_enemies:
                Col_Bullet_Player=pygame.sprite.spritecollide(e,bullets,True)
                for Col in Col_Bullet_Player:

                    if player1.is_angel:
                        e.salud-=20
                        e.is_atacking=True
                    else:
                        e.salud-=10
                        e.is_atacking=True
                    if e.salud <= 0:
                        All_enemies.remove(e)
                        all_elements.remove(e)
                        Background_elements.remove(e)
                    e.objetive=1
                textEnemys=vidaP1.render(str(e.salud),False,[255,255,255])
                screen.blit(textEnemys,[e.rect.x,e.rect.y])
                windows.show()
            for e in All_enemies2:
                Col_Bullet_Player=pygame.sprite.spritecollide(e,bullets,True)
                for Col in Col_Bullet_Player:

                    if player1.is_angel:
                        e.salud-=20
                        e.is_atacking=True
                    else:
                        e.salud-=10
                        e.is_atacking=True

                    if e.salud <= 0:
                        e.is_atacking=False
                        All_enemies2.remove(e)
                        all_elements.remove(e)
                        Background_elements.remove(e)
                        player1.combat=False
                    e.objetive=1
                if e.salud>0:
                    textEnemys=vidaP1.render(str(e.salud),False,[255,255,255])
                    screen.blit(textEnemys,[e.rect.x,e.rect.y])
                    windows.show()
            #balas jugador y boss
            for a in All_Bosses:
                Col_Bullet_Player=pygame.sprite.spritecollide(a,bullets,True)
                for Col in Col_Bullet_Player:
                    if a.salud <=0 :
                        a.is_die=True
                        all_elements.remove(a)
                        All_enemies2.remove(a)
                        Background_elements.remove(a)
                        player1.combat=False
                    elif player1.is_angel and CALACAS==3:
                        a.salud-=20
                        a.is_atacking=True
                        All_enemies2.add(a)
                    elif CALACAS==3:
                        a.salud-=10
                        a.is_atacking=True
                        All_enemies2.add(a)
                textEnemys=vidaP1.render(str(a.salud),False,[255,255,255])
                screen.blit(textEnemys,[a.rect.x,a.rect.y])
                windows.show()
            #jugador contra enemigos
            for p in players:
                Col_E_P=pygame.sprite.spritecollide(p,All_enemies,True)
                for Col in Col_E_P:
                    p.salud-=30
            #balas paredes
            for w in walls:
                Col_B_W=pygame.sprite.spritecollide(w,bullets,True)
            #enemigos paredes
            for e in All_enemies2:
                Col_E_W=pygame.sprite.spritecollide(e,walls,False)
                for m in Col_E_W:
                    if  e.vel_y < 0 and e.rect.top < m.rect.bottom:
                        e.vel_y=2
                    elif e.vel_y > 0 and e.rect.bottom > m.rect.top:
                        e.vel_y=-2
            #balas de enemigos y jugadores

            Col_P_E=pygame.sprite.spritecollide(player1,bullets_enemies2,True)
            for col in Col_P_E:
                if player1.salud > 0:
                    player1.salud-=10
            Col_P_E=pygame.sprite.spritecollide(player2,bullets_enemies2,True)
            for col in Col_P_E:
                if player2.salud > 0:
                    player2.salud-=10

            for P in players:
                Col_P_B=pygame.sprite.spritecollide(P,BulletsSpider,True)
                for COl in Col_P_B:
                    P.salud-=50
            for P in players:
                Col_P_E=pygame.sprite.spritecollide(P,All_enemies2,True)
                for Col in Col_P_E:
                    P.salud-=1000
                if P.salud<=0:
                    close=True

            #removiendo balas
            for B in bullets:
                if B.rect.x <= 0 or B.rect.x > SIZE_SCREEN[0] or B.rect.y <= 0 or B.rect.y > SIZE_SCREEN[1]:
                    bullets.remove(B)
                    all_elements.remove(B)
            for p in players:
                col_miniadds=pygame.sprite.spritecollide(p,miniAdds,True)
                for Col in col_miniadds:
                    p.salud-=15
            for mini in miniAdds:
                col_B_miniadds=pygame.sprite.spritecollide(mini,bullets,True)
                for Col in col_B_miniadds:
                    if mini.salud > 0:
                        mini.salud-=10
                    else:
                        all_elements.remove(mini)
                        miniAdds.remove(mini)
            #enemigos
            for a in All_enemies:
                if a.is_atacking:
                    player1.combat=True
            for a in All_enemies2:
                if a.is_atacking:
                    player1.combat=True

            #movimiento de la pantalla
            if not player1.combat  and not  player2.combat:
                if player2.rect.x > SIZE_SCREEN[0] and player1.rect.x >SIZE_SCREEN[0] :
                    for i in range(700):
                        for B in Background_elements:
                            B.rect.x-=1
                        for  A in All_enemies2:
                            A.vel_y=0
                        player2.vel_x=0
                        player1.vel_x=0
                        player2.rect.x-=1
                        player1.rect.x-=1
                        player1.DOWN=False
                        player1.UP=False
                        player1.RIGHT=False
                        player1.LEFT=False
                        player2.DOWN=False
                        player2.UP=False
                        player2.RIGHT=False
                        player2.LEFT=False
                        Background_elements.update()
                        all_elements.update()
                        windows.clear(screen)
                        Background_elements.draw(screen)
                        all_elements.draw(screen)
                        windows.show()
                    for  A in All_enemies2:
                        A.vel_y=1
                if player2.rect.x < 0 and player1.rect.x < 0:
                    for i in range(700):
                        for B in Background_elements:
                            B.rect.x+=1
                        for  A in All_enemies2:
                            A.vel_y=0
                        player2.vel_x=0
                        player1.vel_x=0
                        player2.rect.x+=1
                        player1.rect.x+=1
                        player1.DOWN=False
                        player1.UP=False
                        player1.RIGHT=False
                        player1.LEFT=False
                        player2.DOWN=False
                        player2.UP=False
                        player2.RIGHT=False
                        player2.LEFT=False
                        Background_elements.update()
                        all_elements.update()
                        windows.clear(screen)
                        Background_elements.draw(screen)
                        all_elements.draw(screen)
                        windows.show()
                    for  A in All_enemies2:
                        A.vel_y=1
                if player2.rect.y >= SIZE_SCREEN[1] and player1.rect.y >= SIZE_SCREEN[1]:
                    for i in range(500):


                        for B in Background_elements:
                            B.rect.y-=1
                        for A in All_enemies2:
                            A.vel_y=0
                        player2.vel_y=0
                        player1.vel_y=0
                        player1.DOWN=False
                        player1.UP=False
                        player1.RIGHT=False
                        player1.LEFT=False
                        player2.DOWN=False
                        player2.UP=False
                        player2.RIGHT=False
                        player2.LEFT=False
                        player2.rect.y-=1
                        player1.rect.y-=1
                        Background_elements.update()
                        all_elements.update()
                        windows.clear(screen)
                        Background_elements.draw(screen)
                        all_elements.draw(screen)
                        windows.show()
                    for  A in All_enemies2:
                        A.vel_y=1
                if player2.rect.y <= 0 and player1.rect.y <= 0:
                    for i in range(500):
                        for B in Background_elements:
                            B.rect.y+=1
                        for A in All_enemies2:
                            A.vel_y=0
                        player2.vel_y=0
                        player1.vel_y=0
                        player2.rect.y+=1
                        player1.rect.y+=1
                        player1.DOWN=False
                        player1.UP=False
                        player1.RIGHT=False
                        player1.LEFT=False
                        player2.DOWN=False
                        player2.UP=False
                        player2.RIGHT=False
                        player2.LEFT=False
                        Background_elements.update()
                        all_elements.update()
                        windows.clear(screen)
                        Background_elements.draw(screen)
                        all_elements.draw(screen)
                        windows.show()
                    for  A in All_enemies2:
                        A.vel_y=1
                if not  functions.Range_enemy(player1.rect.x,player1.rect.y,player2.rect.x,player2.rect.y,20):
                    if player1.rect.x >= SIZE_SCREEN[0]:
                        player1.rect.x-=30
                    if player2.rect.x > SIZE_SCREEN[0]:
                        player2.rect.x-=30
                    if player1.rect.y >= SIZE_SCREEN[1]:
                        player1.rect.y-=30
                    if player2.rect.y > SIZE_SCREEN[1]:
                        player2.rect.y-=30
                    if player1.rect.x <= 0:
                        player1.rect.x+=30
                    if player2.rect.x <=0:
                        player2.rect.x+=30
                    if player1.rect.y <= 0:
                        player1.rect.y+=30
                    if player2.rect.y <=0:
                        player2.rect.y+=30
            if player1.combat:
                if player1.rect.x >= SIZE_SCREEN[0]:
                    player1.rect.x-=30
                if player2.rect.x >= SIZE_SCREEN[0]:
                    player2.rect.x-=30
                if player1.rect.y >= SIZE_SCREEN[1]:
                    player1.rect.y-=30
                if player2.rect.y >= SIZE_SCREEN[1]:
                    player2.rect.y-=30
                if player1.rect.x < 0:
                    player1.rect.x-=30
                if player2.rect.x < 0:
                    player2.rect.x-=30
                if player1.rect.y < 0:
                    player1.rect.y+=30
                if player2.rect.y < 0:
                    player2.rect.y+=30
                player1.combat=False
                player2.combat=False


            #movimiento de los adds y comportamiento de los adda
            for e in All_enemies:
                if functions.Range_enemy(e.rect.x,e.rect.y,player2.rect.x,player2.rect.y,100):
                    e.is_atacking=True
                    e.objetive=2
                if functions.Range_enemy(e.rect.x,e.rect.y,player1.rect.x,player1.rect.y,100):
                    e.is_atacking=True
                    e.objetive=1
            for e in All_enemies :
                if e.is_atacking and e.objetive==2:
                    if player2.rect.x < e.rect.x :
                        e.vel_x=-1
                    if player2.rect.x > e.rect.x:
                        e.vel_x=1
                    if player2.rect.y < e.rect.y:
                        e.vel_y=-1
                    if player2.rect.y > e.rect.y:
                        e.vel_y=1
                if e.is_atacking and e.objetive==1:
                    if player1.rect.x < e.rect.x :
                        e.vel_x=-1
                    if player1.rect.x > e.rect.x:
                        e.vel_x=1
                    if player1.rect.y < e.rect.y:
                        e.vel_y=-1
                    if player1.rect.y > e.rect.y:
                        e.vel_y=1
            for a in All_Bosses:
                if functions.Range_enemy(a.rect.x,a.rect.y,player1.rect.x,player1.rect.y,100) and CALACAS==3:
                    a.is_atacking=True

            #boss medium
            for Boss in All_Bosses:
                if Boss.coldownWeb==0:
                    B=Bullets_spider(imgSkill)
                    B.rect.x=Boss.rect.x
                    B.rect.y=Boss.rect.y
                    B.objetivo_x=player2.rect.x
                    B.objetivo_y=player2.rect.y
                    all_elements.add(B)
                    BulletsSpider.add(B)
                    B=Bullets_spider(imgSkill)
                    B.rect.x=Boss.rect.x
                    B.rect.y=Boss.rect.y
                    B.objetivo_x=player1.rect.x
                    B.objetivo_y=player1.rect.y
                    all_elements.add(B)
                    BulletsSpider.add(B)
                    Boss.coldownWeb=500
                if Boss.coldownAdds==0:
                    i=0
                    for j in range (10):
                        M=adds_miniboss(m2MBoss,rx(),ry(),i)
                        all_elements.add(M)
                        miniAdds.add(M)
                        i+=1
                    Boss.coldownAdds=500
            for a in miniAdds:
                if a.ID % 2 == 0:
                    if player1.rect.x < a.rect.x:
                        a.vel_x=-5
                    if player1.rect.x > a.rect.x:
                        a.vel_x=5
                    if player1.rect.y < a.rect.y:
                        a.vel_y=-5
                    if player1.rect.y > a.rect.y:
                        a.vel_y=5
                else:
                    if player2.rect.x < a.rect.x:
                        a.vel_x=-5
                    if player2.rect.x > a.rect.x:
                        a.vel_x=5
                    if player2.rect.y < a.rect.y:
                        a.vel_y=-5
                    if player2.rect.y > a.rect.y:
                        a.vel_y=5


            for boss in All_Bosses:
                if boss.is_die:
                    for B in BulletsSpider:
                        BulletsSpider.remove(B)
                        all_elements.remove(B)
                    win=True
                    close=True

            for a in All_enemies2:
                if functions.Range_enemy(a.rect.x,a.rect.y,player1.rect.x,player1.rect.y,100):
                    a.is_atacking=True
                    a.objetive=1
                if functions.Range_enemy(a.rect.x,a.rect.y,player2.rect.x,player2.rect.y,100):
                    a.is_atacking=True
                    a.objetive=2
            for a in All_enemies2:
                if a.coldownWeb==0 :
                    B=Bullets_enemies2(img_adds2)
                    B.rect.x=a.rect.x
                    B.rect.y=a.rect.y
                    B.objetivo_x=player1.rect.x
                    B.objetivo_y=player1.rect.y
                    all_elements.add(B)
                    bullets_enemies2.add(B)
                    B=Bullets_enemies2(img_adds2)
                    B.rect.x=a.rect.x
                    B.rect.y=a.rect.y
                    B.objetivo_x=player2.rect.x
                    B.objetivo_y=player2.rect.y
                    all_elements.add(B)
                    bullets_enemies2.add(B)
                    a.coldownWeb=300
                if a.coldownAdds==0:
                    for i in range(6):
                        en=enemies(e1,rx(),ry())
                        en.is_atacking=True
                        en.objetive=robjetive() # modidicador de objetivo
                        all_elements.add(en)
                        All_enemies.add(en)
                        a.coldownAdds=500
            for B in bullets_enemies2:
                if functions.Range_enemy(B.rect.x,B.rect.y,B.objetivo_x,B.objetivo_y,10):
                    bullets_enemies2.remove(B)
                    all_elements.remove(B)
            salud_player1="Player1 " + str(player1.salud)
            salud_player2="Player2 " + str(player2.salud)
            Calaveras="Calaveras : " + str(CALACAS)
            text=vidaP1.render(salud_player1,False,[255,255,255])
            text2=vidaP1.render(salud_player2,False,[255,255,255])
            Name1=vidaP1.render("Kalcicko",False,[255,255,255])
            Name2=vidaP1.render("Kasandra",False,[255,255,255])
            Calaveras=vidaP1.render(Calaveras,False,[255,255,255])

            Background_elements.update()
            all_elements.update()
            All_enemies.update()
            All_enemies2.update()
            windows.clear(screen)
            Background_elements.draw(screen)
            all_elements.draw(screen)
            screen.blit(text,[10,10])
            screen.blit(text2,[400,10])
            screen.blit(Name1,[player1.rect.x,player1.rect.y-30])
            screen.blit(Name2,[player2.rect.x,player2.rect.y-30])
            screen.blit(Calaveras,[SIZE_SCREEN[0]/2,40])
            COLORp1=[155,0,0]
            COLORp2=[155,0,0]
            if player1.salud<30:
                COLORp1=[255,0,0]
            if player2.salud<50:
                COLORp2=[255,0,0]
            pygame.draw.line(screen,COLORp1,[player1.rect.x,player1.rect.y-5],[player1.rect.x+player1.salud,player1.rect.y-5],10)
            pygame.draw.line(screen,COLORp2,[player2.rect.x,player2.rect.y-5],[player2.rect.x+player2.salud,player2.rect.y-5],10)
            windows.show()
            #clock.tick(20)
            #changes

main()
