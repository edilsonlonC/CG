from principal_objects.objects import Enemies

class enemies(Enemies):
    def __init__(self,m,x,y):
        Enemies.__init__ (self,m)
        self.rect.x=x
        self.rect.y=y
        self.salud=20
        self.ID=0
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

class enemies2 (Enemies):
    def __init__(self,m,x,y):
        Enemies.__init__(self,m)
        self.rect.x=x
        self.rect.y=y
        self.salud=40
        self.objetivoX=0
        self.objetivoY=0
        self.vel_y=1
        self.coldownWeb=1
        self.objetivo_x=0
        self.objetivo_y=0
        self.salud=50
        self.vel_y=-2
        self.coldownAdds=1
    def update (self):
        if self.is_atacking:
            if self.coldownWeb>0:
                self.coldownWeb-=1
            if self.coldownAdds>0:
                self.coldownAdds-=1
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

class Miniboss(Enemies):
    def __init__(self,m,x,y):
        Enemies.__init__(self,m)
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





class adds_miniboss (Enemies):
    def __init__(self,m,x,y,ID):
        Enemies.__init__(self,m)
        self.rect.x=x
        self.rect.y=y
        self.salud=-20
        self.ID=ID
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
