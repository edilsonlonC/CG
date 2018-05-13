
import pygame
import random
r=lambda: random.randint(0,255)
from Windows import windows as W
def Range_enemy (enemy_x,enemy_y,player_x,player_y,Range_atacking):
    if player_x > enemy_x-Range_atacking and player_x < enemy_x+Range_atacking and player_y > enemy_y-Range_atacking and player_y < enemy_y+Range_atacking:
        return True
def Menu (screen):
    img=W.Create_images('Menu/fondo.jpeg')
    img2=W.Create_images('Menu/fondo2.jpeg')
    W.show_images(screen,img,[0,0])
    W.show_images(screen,img2,[400,0])
    text_menu = pygame.font.Font('freesansbold.ttf',32)
    text=text_menu.render("SPACE TO START",False,[r(),r(),r()])
    text2=text_menu.render("ESC TO EXIT",False,[r(),r(),r()])
    screen.blit(text,[300,250])
    screen.blit(text2,[300,300])
