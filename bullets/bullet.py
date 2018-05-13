from principal_objects.objects import Bullets
class Bullet_player (Bullets):
    def __init__(self,m):
        Bullets.__init__(self,m)
        self.time=0
    def update (self):
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
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
