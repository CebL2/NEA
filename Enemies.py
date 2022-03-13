import pygame, random
import numpy as np

class Enemy(pygame.sprite.Sprite):
    #Enemy  = pygame.Surface((200,200)) #pygame.image.load("spritegroup//test enemy.png").convert()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.playerx = 1
        #self.ObstacleClass = obstacle
        self.playery = 1
        self.image = pygame.Surface((100,100)) #Enemy.Enemy
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(0,1280),(random.randint(0,1024))))   
        self.health = random.randint(1,5)
        self.difficulty = 1
        #self.bosshealth = 10
        self.speed = 10
  
   #1840x1000 
   
   #this is the amount of space that can be worked with 
#  def drawgrid(self,posx,posy):
#             for y, row in enumerate(self.map):  #element, value
#             for x , col in enumerate(row):
                
#                 #for every direction
#                 xval = x*self.xval
#                 yval = y*self.yval
#                 if y == posx and x == posy:

#                     self.traversedlist[y][x] = 1
    
    def PathFind(self,x,y):
        xval = 1840//len(self.map[0])
        yval = 1000//len(self.map)
        xdist= self.rect.x - x
        ydist = self.rect.y - y
        #for y, 
        
        
        
        #get the distance between the enemy and player
        #in that distance check whether if in that path there is an obstacle 
        
        pass
   
    #we can parse in a obstacle object by default so that it can be accessed at any time, then based on the values of the obstacle size and center, the enemy can then move 
    #away from the obstacle or try new paths to get to the enemy
    def update(self,x,y): #simple enemy movement to move to player

        
        
        xdist= self.rect.x - x
        ydist = self.rect.y - y
        #print(xdist,ydist)
        
        
        
        if xdist > 0:
            self.rect.x-=1
            
        elif xdist <0 :
            self.rect.x+=1
            
        elif  ydist>0:
            self.rect.y-=1
           
        elif  ydist<0:
            self.rect.y +=1

class Boss(Enemy):
    def __init__(self, obstacle):
        super().__init__(obstacle)
        self.health = 10
        
            
        