import pygame 
class Attack(pygame.sprite.Sprite): 
    def __init__(self,unitsize,unitx,unity,screenx,screeny,Direction): #takes in the unit's x and y position, the width and length of the screen, and the direction
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (unitx,unity)
        self.speed = 15
        self.Direction = Direction
        self.screenx = screenx
        self.screeny = screeny
        self.unitsize = unitsize
        
        if self.Direction == 1:
            self.rect.centery -=self.unitsize  #based what the value of the direction is passed in, the position of where the projectile is shot from is determined by their size
        elif self.Direction ==2:
            self.rect.centerx+=self.unitsize
        elif self.Direction == 3:
            self.rect.centerx-=self.unitsize
        else:
            self.rect.centery+=self.unitsize
        
    def update(self):
        if self.Direction == 1:     
            self.rect.y -= self.speed
            if self.rect.y < 40: #this specific value is used as 40 is how thick the borders are 
                self.kill() #if the position component of the projectile goes beyond the specified value, remove the projectile
        elif self.Direction == 2:
            self.rect.x += self.speed
            if self.rect.x > self.screenx-40:
                self.kill()
        elif self.Direction == 3:
            self.rect.x -= self.speed
            if self.rect.x < 40:
                self.kill()
        else:
            self.rect.y += self.speed
            if self.rect.y > self.screeny-40:
                self.kill()