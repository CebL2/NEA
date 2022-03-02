from tkinter.messagebox import NO
import pygame, random


#pos, size
class RoomObstacles(pygame.sprite.Sprite):
    def __init__(self,i,j,xsize=None,ysize=None,xcenter=None,ycenter = None): #map indexes
        pygame.sprite.Sprite.__init__(self)
        self.i = i
        self.j = j
        #self.amount = amount
        
        # self.xsize = xsize
        # self.ysize = ysize
        # self.xcenter = xcenter
        # self.ycenter =ycenter
        if xsize == None:
            self.xsize = random.randint(200,600)
            self.ysize= random.randint(200,800)
            self.xcenter=random.randint(500,1000)
            self.ycenter= random.randint(500,1000)
        else:
            self.xsize = xsize
            self.ysize= ysize
            self.xcenter= xcenter
            self.ycenter=  ycenter
        
        #amount = random.randint(3,6)
        #for _ in range(0,amount):
        
        self.image = pygame.Surface((self.xsize,self.ysize))
        #self.ObstacleGroup = pygame.sprite.Group()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.xcenter,self.ycenter)  

        
        #self.rect.center = (300,500)
    
    

