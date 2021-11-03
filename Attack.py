import pygame 

screenx = 1280
screeny = 1024
screen = pygame.display.set_mode((screenx,screeny))
class Attack(pygame.sprite.Sprite):
    projectile = pygame.image.load("spritegroup//projectile.png").convert()
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Attack.projectile
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 10
    
    def update(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_DOWN]:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()

        # if keypressed[pygame.K_a]
        #     player.moveleft()
        # if keypressed[pygame.K_d]:
        #     player.moveright()
        # if keypressed[pygame.K_w] > 
    
    
        
        
        

        
        
        