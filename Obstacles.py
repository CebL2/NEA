import pygame, random


#pos, size
class RoomObstacles(pygame.sprite.Sprite):
    def __init__(self,i,j):
        pygame.sprite.Sprite.__init__(self)
        self.i = i
        self.j = j
        #amount = random.randint(3,6)
        #for _ in range(0,amount):
        self.image = pygame.Surface((random.randint(100,200),random.randint(100,200)))
        #self.ObstacleGroup = pygame.sprite.Group()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(500,1000),(random.randint(500,1000))))  
        #self.rect.center = (300,500)
    
    

