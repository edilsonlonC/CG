from principal_objects.objects import Player1
VELOCIDAD=5
class TANK (Player1):
    def __init__ (self,m):
        Player1.__init__(self,m)
        self.salud=80
    def update (self):
        if self.is_run:

            if self.move<3 and not self.is_k_up:
                self.move+=1
            else:
                self.move=0

            if self.time>0:
                self.time-=1
            else:
                self.time=5


        if  self.coldown >0:
            self.coldown-=1
        if self.is_angel and self.time_angel > 0:
            self.time_angel-=1

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
class HEALER (Player1):
    def __init__ (self,m):
        Player1.__init__(self,m)
        self.salud=100
    def update (self):
        if self.is_run:

            if self.move<3 and not self.is_k_up:
                self.move+=1
            else:
                self.move=0

            if self.time>0:
                self.time-=1
            else:
                self.time=5


        if  self.coldown >0:
            self.coldown-=1
        if self.is_angel and self.time_angel > 0:
            self.time_angel-=1

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
