import pygame
import windows
import ConfigParser
#cut image
#img is image than want cut
# x and y are a element than u want
#elementsX and elementsY are the total elements in image
def image_cut (img,x,y,elementsX,elementsY):
    info=img.get_rect()
    an_img = info[2]
    al_img = info[3]
    an_corte = int(an_img/elementsX)
    al_corte = int(al_img/elementsY)
    cuadro = img.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
    return cuadro
#this function insert images in a list
def insert_in_list (img,limitx,limity,N_elementsX,N_elementsY):
    List_Elements=[]
    for i in range (limitx):
        image=image_cut(img,i,limity,N_elementsX,N_elementsY)
        List_Elements.append(image)
    return List_Elements
#this funcion insert in a list more lists of images
#img is the complete image than u want cut
#N_elementsX and N_elementsY is the number  total of elements in the image
def insert_in_matrix (img,N_elementsX ,N_elementsY):
    Matriz_Elements=[]
    for i in range(N_elementsY):
        List_Elements=insert_in_list(img,N_elementsX,i,N_elementsX,N_elementsY)
        Matriz_Elements.append(List_Elements)
    return Matriz_Elements
