import pygame
class Player1 (pygame.sprite.Sprite):
    def __init__ (self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.action=0
        self.move=0
        self.image=self.m[self.action][self.move]
        self.rect=self.image.get_rect()
        self.rect.x=60
        self.rect.y=1400
        self.vel_x=0
        self.vel_y=0
        self.is_k_up=False # pregiuntar si ha dejado de presionar teclas
        self.time=5
        self.disparar=True # determinar cuando esta disparando
        self.is_atacking=False ## para poner limite de tiempo a los angeles
        self.is_angel=False
        self.time_angel=0
        self.is_run=False
        self.coldown=0
        self.DOWN,self.UP,self.LEFT,self.RIGHT=False,False,False,False
        self.combat=False

class Bullets (pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.image=m
        self.rect=self.image.get_rect()
        self.vel_x=1
        self.vel_y=1

class Enemies (pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.action=0
        self.move=0
        self.image=self.m[self.action][self.move]
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.vel_x=0
        self.vel_y=0
        self.is_atacking=False
        self.objetive=0
        self.ID=0
