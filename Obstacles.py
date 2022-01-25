import pygame, random

screenx = 1920
screeny = 1080
screen = pygame.display.set_mode((screenx,screeny))

#for every room inside the grid:
    #assign a room obstacle  class to it


# j = RoomObstacles
# 
Black = (0,0,0)

#pos, size
class RoomObstacles(pygame.sprite.Sprite):
    def __init__(self,i,j):
        pygame.sprite.Sprite.__init__(self)
        self.i = i
        self.j = j

        self.image = pygame.Surface((100,100))
        #self.ObstacleGroup = pygame.sprite.Group()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(0,1280),(random.randint(0,1024))))  
        #self.rect.center = (300,500)
    
    

