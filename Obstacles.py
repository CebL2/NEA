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
    Obstacles = pygame.Surface((random.randint(0,100),random.randint(0,100)))
    Obstacles.fill((0,0,0))
    def __init__(self) -> None:
        super().__init__()
        self.image = RoomObstacles.Obstacles
        #ObstacleGroup = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.center = (300,500)
        
        
        
        
        
      
        
        
        

        
