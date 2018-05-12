import pygame
from Windows import windows,functions
from Windows import cut
from Windows.objects import Player1 , Bullets , Enemys
import ConfigParser
SIZE_SCREEN=[700,500]
VELOCIDAD=5
pygame.init()
"""
Cosas que faltan.
1) crear mapa completo (Falta aun)
2) llenar los respectivos grupos con los elementos (ya)
3) comportamiento de los enemigos (ya)
4) crear coliciones:
    balas_jugadores vs enemigos (realizado)
    balas_enemigos vs jugadores (realizado)
    muros vs enemigos y jugadores (realizado)
    jugadores contra enemigos (realizado)
5) crear miniboss y configurar comportamiento (realizado)
6) crear boss final (en proceso)
7) mejoras en aspectos del videojuego
8) agregar los modificaores correspondientes (me faltan 2)



"""
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

class TANK (Player1):
    def __init__ (self,m):
        Player1.__init__(self,m)
        self.salud=50
    def update (self):
        if self.is_run:
            if  self.coldown >0:
                self.coldown-=1
            if self.is_angel and self.time_angel > 0:
                self.time_angel-=1
            if self.move<3 and not self.is_k_up:
                self.move+=1
            else:
                self.move=0

            if self.time>0:
                self.time-=1
            else:
                self.time=5


        if not self.RIGHT :
            self.vel_x=0
            self.is_run=False
        if not self.LEFT :
            self.vel_x=0
            self.is_run=False
        if not self.UP :
            self.vel_y=0
            self.is_run=False
        if not self.DOWN :
            self.vel_y=0
            self.is_run=False

        if self.UP:
            self.vel_y=-VELOCIDAD
            self.vel_x=0
            self.action=3
            self.is_run=True

        if self.DOWN:
            self.vel_y=VELOCIDAD
            self.vel_x=0
            self.action=0
            self.is_run=True

        if self.LEFT:
            self.vel_x=-VELOCIDAD
            self.vel_y=0
            self.action=1
            self.is_run=True
        if self.RIGHT :
            self.vel_x=VELOCIDAD
            self.vel_y=0
            self.action=2
            self.is_run=True
        self.rect.x+=self.vel_x
        print self.rect.x
        self.rect.y+=self.vel_y
        self.image=self.m[self.action][self.move]




class HEALER (Player1):
    def __init__ (self,m):
        Player1.__init__(self,m)
        self.salud=50
    def update (self):
        if self.is_run:
            if  self.coldown >0:
                self.coldown-=1
            if self.is_angel and self.time_angel > 0:
                self.time_angel-=1
            if self.move<3 and not self.is_k_up:
                self.move+=1
            else:
                self.move=0

            if self.time>0:
                self.time-=1
            else:
                self.time=5


        if not self.RIGHT :
            self.vel_x=0
            self.is_run=False
        if not self.LEFT :
            self.vel_x=0
            self.is_run=False
        if not self.UP :
            self.vel_y=0
            self.is_run=False
        if not self.DOWN :
            self.vel_y=0
            self.is_run=False

        if self.UP:
            self.vel_y=-VELOCIDAD
            self.vel_x=0
            self.action=3
            self.is_run=True

        if self.DOWN:
            self.vel_y=VELOCIDAD
            self.vel_x=0
            self.action=0
            self.is_run=True

        if self.LEFT:
            self.vel_x=-VELOCIDAD
            self.vel_y=0
            self.action=1
            self.is_run=True
        if self.RIGHT :
            self.vel_x=VELOCIDAD
            self.vel_y=0
            self.action=2
            self.is_run=True
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        self.image=self.m[self.action][self.move]

class Bullet_player (Bullets):
    def __init__(self,m):
        Bullets.__init__(self,m)
        self.time=0
    def update (self):
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y

class DPS (Player1):
    def __init__ (self):
        pass
    def update (self):
        pass

class enemies(Enemys):
    def __init__(self,m,x,y):
        Enemys.__init__ (self,m)
        self.rect.x=x
        self.rect.y=y
        self.salud=100
    def update (self):
        if self.vel_x>0:
            self.action=2
        if self.vel_x<0:
            self.action=1
        if self.vel_y<0:
            self.action=3
        if self.vel_y>0:
            self.action=0
        if self.move <3:
            self.move+=1
        else :
            self.move=0
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        self.image=self.m[self.action][self.move]

class enemies2 (Enemys):
    def __init__(self,m,x,y):
        Enemys.__init__(self,m)
        self.rect.x=x
        self.rect.y=y
        self.salud=40
        self.objetivoX=0
        self.objetivoY=0
        self.vel_y=1
        self.coldownWeb=1
        self.objetivo_x=0
        self.objetivo_y=0
        self.salud=100
        self.vel_y=-2
    def update (self):
        if self.is_atacking:
            if self.coldownWeb>0:
                self.coldownWeb-=1
        if self.vel_x>0:
            self.action=2
        if self.vel_x<0:
            self.action=1
        if self.vel_y<0:
            self.action=3
        if self.vel_y>0:
            self.action=0
        if self.move <3:
            self.move+=1
        else :
            self.move=0
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        self.image=self.m[self.action][self.move]

class Miniboss(Enemys):
    def __init__(self,m,x,y):
        Enemys.__init__(self,m)
        self.rect.x=x
        self.rect.y=y
        self.objetivoX=0
        self.objetivoY=0
        self.vel_y=1
        self.salud=500
        self.is_atacking=False
        self.coldownWeb=1
        self.coldownAdds=1
        self.is_die=False
    def update (self):

        if self.is_atacking:
            if self.vel_x>0:
                self.action=2
            if self.vel_x<0:
                self.action=1
            if self.vel_y<0:
                self.action=3
            if self.vel_y>0:
                self.action=0
            if self.move <3:
                self.move+=1
            else :
                self.move=0
            if self.coldownAdds > 0:
                self.coldownAdds-=1
            if self.coldownWeb > 0:
                self.coldownWeb-=1
            self.rect.x+=self.vel_x
            self.rect.y+=self.vel_y
            self.image=self.m[self.action][self.move]

class Bullets_spider(Bullets):
    def __init__ (self,m):
        Bullets.__init__(self,m)
        self.objetivo_x=0
        self.objetivo_y=0
    def update (self):
        if self.rect.x > self.objetivo_x:
            self.vel_x=-10
        if self.rect.x < self.objetivo_x:
            self.vel_x=10
        if self.rect.y < self.objetivo_y:
            self.vel_y=10
        if self.rect.y > self.objetivo_y:
            self.vel_y=-10
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y

class Bullets_enemies2(Bullets):
    def __init__ (self,m):
        Bullets.__init__(self,m)
        self.objetivo_x=0
        self.objetivo_y=0
    def update (self):
        if self.rect.x > self.objetivo_x:
            self.vel_x=-10
        if self.rect.x < self.objetivo_x:
            self.vel_x=10
        if self.rect.y < self.objetivo_y:
            self.vel_y=10
        if self.rect.y > self.objetivo_y:
            self.vel_y=-10
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y

class adds_miniboss (Enemys):
    def __init__(self,m,x,y):
        Enemys.__init__(self,m)
        self.rect.x=x
        self.rect.y=y
    def update (self):
            if self.vel_x>0:
                self.action=2
            if self.vel_x<0:
                self.action=1
            if self.vel_y<0:
                self.action=3
            if self.vel_y>0:
                self.action=0
            if self.move <2:
                self.move+=1
            else:
                self.move=0
            self.rect.x+=self.vel_x
            self.rect.y+=self.vel_y
            self.image=self.m[self.action][self.move]





def main ():
    n=0
    vidaP1=pygame.font.Font(None,32)
    #screen for gane
    screen=windows.Create_screen(SIZE_SCREEN)
    close=False
    #read map and info of file extern
    inter=ConfigParser.ConfigParser()
    inter.read('mapa.map')
    img=windows.Create_images('terrenogen.png')
    _map=inter.get('nivel','mapa')
    _Maps=_map.split('\n')
    M1=cut.insert_in_matrix(img,32,12)
    #finish read
    #start images
    img1=windows.Create_images('char2.png')
    img2=windows.Create_images('posiblepersonaje.png')
    img2angel=windows.Create_images('angelhealer.png')
    img_bullet_haler=windows.Create_images('spell_basic.png')
    img_e=windows.Create_images('adds2.png')
    img_e2=windows.Create_images('adds5.png')
    img_Boss=windows.Create_images('bossmedium.png')
    img1angel=windows.Create_images('angeldps.png')
    img_bullet_A=windows.Create_images('spell.png')
    imgSkill=windows.Create_images('SkillMiniboss.png')
    img3miniadds=windows.Create_images('image2.png')
    img_adds2=windows.Create_images('spellsAdds2.png')
    #finish images
    #Cut images
    m1=cut.insert_in_matrix(img1,6,4)
    m2=cut.insert_in_matrix(img2,4,4)
    m2Angel=cut.insert_in_matrix(img2angel,4,4)
    m1Angel=cut.insert_in_matrix(img1angel,4,4)
    e1=cut.insert_in_matrix(img_e,4,4)
    e2=cut.insert_in_matrix(img_e2,4,4)
    boss1=cut.insert_in_matrix(img_Boss,4,4)
    Miniadds=cut.insert_in_matrix(img3miniadds,3,4)
    #finish cuting images
    #create objects
    player1=HEALER(m1)
    player2=TANK(m2)
    #finisg objects
    #creating groups
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
    all_elements.add(player1)
    all_elements.add(player2)
    players.add(player1)
    players.add(player2)
    clock=pygame.time.Clock()
    x=0
    y=0
    #ciclo para la lectura del mapa
    for i in range (len(_Maps)):
        x=0
        for m in _Maps[i]:
            element_X=int(inter.get(m,'x'))
            element_y=int (inter.get(m,'y'))
            B=Background(x,y,M1[element_y][element_X])
            Background_elements.add(B)
            x+=32
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
                All_enemies2.add(en)
                Background_elements.add(en)
                All_Bosses.add(en)


        y+=32
    while not close:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                close=True


        #player1 move
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

                if events.key==pygame.K_1:
                    if player1.salud < 100:
                        if player2.is_angel:
                            player1.salud+=15
                        else:
                            player1.salud+=5
                if events.key==pygame.K_2:
                    if player2.salud < 80:
                        if player2.is_angel:
                            player2.salud+=15
                        else:
                            player2.salud+=5
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
                if e.salud < 0:
                    All_enemies.remove(e)
                    all_elements.remove(e)
                elif player1.is_angel:
                    e.salud-=20
                    e.is_atacking=True
                else:
                    e.salud-=10
                    e.is_atacking=True
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
                if e.salud < 0:
                    e.is_atacking=False
                    All_enemies2.remove(e)
                    all_elements.remove(e)
                    Background_elements.remove(e)
                    player1.combat=False
            if e.salud>0:
                textEnemys=vidaP1.render(str(e.salud),False,[255,255,255])
                screen.blit(textEnemys,[e.rect.x,e.rect.y])
                windows.show()
        for a in All_Bosses:
            Col_Bullet_Player=pygame.sprite.spritecollide(a,bullets,True)
            for Col in Col_Bullet_Player:
                if a.salud <=0:
                    a.is_die=True
                    all_elements.remove(a)
                    All_enemies2.remove(a)
                    player1.combat=False
                elif player1.is_angel:
                    a.salud-=20
                    a.is_atacking=True
                else:
                    a.salud-=10
                    a.is_atacking=True
            textEnemys=vidaP1.render(str(a.salud),False,[255,255,255])
            screen.blit(textEnemys,[a.rect.x,a.rect.y])
            windows.show()
        #jugador contra enemigos
        for p in players:
            Col_E_P=pygame.sprite.spritecollide(p,All_enemies,True)
            for Col in Col_E_P:
                p.salud-=40
        #balas paredes
        for w in walls:
            Col_B_W=pygame.sprite.spritecollide(w,bullets,True)
        #enemigos parede
        for e in All_enemies2:
            Col_E_W=pygame.sprite.spritecollide(e,walls,False)
            for m in Col_E_W:
                if  e.vel_y < 0 and e.rect.top < m.rect.bottom:
                    e.vel_y=2
                elif e.vel_y > 0 and e.rect.bottom > m.rect.top:
                    e.vel_y=-2
        #balas de enemigos y jugadores
        for P in players:
            Col_P_E=pygame.sprite.spritecollide(P,bullets_enemies2,True)
            for col in Col_P_E:
                if p.salud > 0:
                    p.salud-=10

        for P in players:
            Col_P_B=pygame.sprite.spritecollide(P,BulletsSpider,True)
            for COl in Col_P_B:
                P.salud-=20
        for P in players:
            Col_P_E=pygame.sprite.spritecollide(P,All_enemies2,True)
            for Col in Col_P_E:
                p.salud-=1000
        for B in bullets:
            if B.rect.x <= 0 or B.rect.x > SIZE_SCREEN[0]:
                bullets.remove(B)

        #enemigos
        for a in All_enemies:
            if a.is_atacking:
                player1.combat=True
        for a in All_enemies2:
            if a.is_atacking:
                player1.combat=True
        #movimiento de la pantalla
        if not player1.combat or not  player2.combat:
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
                for i in range(200):


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
                for i in range(200):
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
        if player1.combat:
            if player1.rect.x >= SIZE_SCREEN[0]:
                player1.rect.x-=30
            if player2.rect.x > SIZE_SCREEN[0]:
                player2.rect.x-=30
            player1.combat=False


        #movimiento e los adds
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
            if functions.Range_enemy(a.rect.x,a.rect.y,player1.rect.x,player1.rect.y,100):
                a.is_atacking=True
        for Boss in All_Bosses:
            if Boss.coldownWeb==0:
                B=Bullets_spider(imgSkill)
                B.rect.x=Boss.rect.x
                B.rect.y=Boss.rect.y
                B.objetivo_x=player1.rect.x
                B.objetivo_y=player1.rect.y
                all_elements.add(B)
                BulletsSpider.add(B)
                Boss.coldownWeb=1000
        for boss in All_Bosses:
            if boss.is_die:
                for B in BulletsSpider:
                    BulletsSpider.remove(B)
                    all_elements.remove(B)
        for a in All_enemies2:
            if functions.Range_enemy(a.rect.x,a.rect.y,player1.rect.x,player1.rect.y,100):
                a.is_atacking=True
                a.objetive=1
            if functions.Range_enemy(a.rect.x,a.rect.y,player2.rect.x,player2.rect.y,100):
                a.is_atacking=True
                a.objetive=2
        for a in All_enemies2:
            if a.coldownWeb==0 and a.objetive==1:
                B=Bullets_enemies2(img_adds2)
                B.rect.x=a.rect.x
                B.rect.y=a.rect.y
                B.objetivo_x=player1.rect.x
                B.objetivo_y=player1.rect.y
                all_elements.add(B)
                bullets_enemies2.add(B)
                a.coldownWeb=100
            if a.coldownWeb==0 and a.objetive==2:
                B=Bullets_enemies2(img_adds2)
                B.rect.x=a.rect.x
                B.rect.y=a.rect.y
                B.objetivo_x=player2.rect.x
                B.objetivo_y=player2.rect.y
                all_elements.add(B)
                bullets_enemies2.add(B)
                a.coldownWeb=100
        for B in bullets_enemies2:
            if functions.Range_enemy(B.rect.x,B.rect.y,B.objetivo_x,B.objetivo_y,30):
                bullets_enemies2.remove(B)
                all_elements.remove(B)
        text=vidaP1.render(str(player1.salud),False,[0,0,0])
        text2=vidaP1.render(str(player2.salud),False,[0,0,0])
        Background_elements.update()
        all_elements.update()
        # All_enemies.update()
        # All_enemies2.update()
        windows.clear(screen)
        Background_elements.draw(screen)
        all_elements.draw(screen)
        screen.blit(text,[10,10])
        screen.blit(text2,[40,10])
        windows.show()
        clock.tick(20)
        #changes

main()
