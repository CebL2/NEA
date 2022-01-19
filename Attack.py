import pygame 

Orange = (255,165,0)
screenx = 1280
screeny = 1024
screen = pygame.display.set_mode((screenx,screeny))
class Attack(pygame.sprite.Sprite):
    projectile =  pygame.Surface((10,10)) #pygame.image.load("spritegroup//projectile.png").convert()
    #projectile.fill(Orange)
    def __init__(self,x,y,Direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = Attack.projectile
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 10
        self.Direction = Direction
    
    def update(self):
        if self.Direction == 1:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()
        elif self.Direction == 2:
            self.rect.x += self.speed
            if self.rect.y < 0:
                self.kill()
        elif self.Direction == 3:
            self.rect.x -= self.speed
            if self.rect.y < 0:
                self.kill()
        else:
            self.rect.y += self.speed
            if self.rect.y > screeny:
                self.kill()
            
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     click = True
        
        


        
        
        

        
        
        