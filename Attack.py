import pygame 



class Attack(pygame.sprite.Sprite):
    projectile =  pygame.Surface((10,10)) #pygame.image.load("spritegroup//projectile.png").convert()
    #projectile.fill(Orange)
    def __init__(self,playerx,playery,screenx,screeny,Direction): #the position of the player, two screen values and the direction of the attack
        pygame.sprite.Sprite.__init__(self)
        self.image = Attack.projectile
        self.rect = self.image.get_rect()
        self.rect.center = (playerx,playery)
        self.speed = 10
        self.Direction = Direction
        self.screenx = screenx
        self.screeny = screeny

    def update(self):
        if self.Direction == 1:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()
        elif self.Direction == 2:
            self.rect.x += self.speed
            if self.rect.x > self.screenx:
                self.kill()
        elif self.Direction == 3:
            self.rect.x -= self.speed
            if self.rect.y < 0:
                self.kill()
        else:
            self.rect.y += self.speed
            if self.rect.y > self.screeny:
                self.kill()
            
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     click = True
        
        


        
        
        

        
        
        