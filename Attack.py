import pygame 

Orange = (255,165,0)
screenx = 1280
screeny = 1024
screen = pygame.display.set_mode((screenx,screeny))
class Attack(pygame.sprite.Sprite):
    projectile =  pygame.Surface((10,10)) #pygame.image.load("spritegroup//projectile.png").convert()
    #projectile.fill(Orange)
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Attack.projectile
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 1
    
    def update(self):
        
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


        
        
        

        
        
        