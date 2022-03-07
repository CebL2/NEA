import pygame, random
import numpy as np

class Enemy(pygame.sprite.Sprite):
    #Enemy  = pygame.Surface((200,200)) #pygame.image.load("spritegroup//test enemy.png").convert()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.playerx = 1
        self.playery = 1
        self.image = pygame.Surface((100,100)) #Enemy.Enemy
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(0,1280),(random.randint(0,1024))))   
        self.health = 2
        self.difficulty = 1
        self.bosshealth = 10
        self.speed = 10
  
    def update(self,x,y,test=None): #simple enemy movement to move to player
        
        xdist= self.rect.x - x
        ydist = self.rect.y - y
        #print(xdist,ydist)
        
        
        #if the enemy collided
        if xdist > 0:
            self.rect.x-=1
            
        elif xdist <0 :
            self.rect.x+=1
            
        elif  ydist>0:
            self.rect.y-=1
           
        elif  ydist<0:
            self.rect.y +=1

