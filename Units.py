
from Attack import *
import random

import pygame 


class Unit(pygame.sprite.Sprite):
    def __init__(self,screenx,screeny,size=None,colour=None):
        pygame.sprite.Sprite.__init__(self) 
        self.screenx = screenx
        self.screeny = screeny
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.rect = self.image.get_rect()
    



class Player(Unit):  #Player class
    def __init__(self,screenx,screeny,size,colour,centerx= None,centery= None):   #screen values are passed in  
        self.centerx = centerx
        self.centery = centery
        super().__init__(screenx,screeny,size,colour)
        
        if self.centerx == None:
            self.rect.center = (self.screenx/2, self.screeny/2)
        else:
            self.rect.center = (self.centerx, self.centery)
        self.state = 1
        self.speed = 10
        self.projectilegroup = pygame.sprite.Group()  #projectile group 
        # self.charClass = charclass
        # self.statblock = statblock
        # self.charlist = charclasslist
    # def PlayerClass(self):
    #     if self.charClass == self.charlist[0]:#warrior #charclass = ["Warrior","Mage","Paladin","Rogue"]
    #         bonuses = Warrior()  #planning to add classes
    #     elif self.charclass == self.charlist[1]:
    #         bonuses = Mage()
    #     elif self.charclass == self.charlist[2]:
    #         bonuses = Paladin()     
    #     else:
    #         bonuses = Rogue()     #add bonuses to statblock
    # def Spell(self,charclass,charlist):
    #     thing = Spells()    
    def update(self):  #update function to move player
        keypressed = pygame.key.get_pressed()
        
        if keypressed[pygame.K_s] and self.rect.y < self.screeny:
            self.rect.y += self.speed
        if keypressed[pygame.K_w] and self.rect.y > 0:
            self.rect.y  -= self.speed
        if keypressed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keypressed[pygame.K_d] and self.rect.x <  self.screenx:
            self.rect.x += self.speed
    def Attackup(self):  #attack functions for projectiles
        projectileup = Attack(self.rect.centerx,self.rect.centery-50,self.screenx,self.screeny,1)
        self.projectilegroup.add(projectileup)

    def Attackright(self):
        projectiledown = Attack(self.rect.centerx+50,self.rect.centery,self.screenx,self.screeny,2)
        self.projectilegroup.add(projectiledown)
        
    def Attackleft(self):
        projectiledown = Attack(self.rect.centerx-50,self.rect.centery,self.screenx,self.screeny,3)
        self.projectilegroup.add(projectiledown)
        
    def Attackdown(self):
        projectiledown = Attack(self.rect.centerx,self.rect.centery+50,self.screenx,self.screeny,4)
        self.projectilegroup.add(projectiledown)
        


class Enemy(Unit):
    #Enemy  = pygame.Surface((200,200)) #pygame.image.load("spritegroup//test enemy.png").convert()
    def __init__(self,screenx,screeny,size,colour):
        super().__init__(screenx,screeny,size,colour)
        self.playerx = 1
        #self.ObstacleClass = obstacle
        self.playery = 1
        #self.image = pygame.Surface((100,100)) #Enemy.Enemy
        #self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(0,1280),(random.randint(0,1024))))   
        self.health = random.randint(1,5)
        self.difficulty = 1
     
        self.speed = 10
  
#    #1840x1000 
   
#    #this is the amount of space that can be worked with 
# #  def drawgrid(self,posx,posy):
# #             for y, row in enumerate(self.map):  #element, value
# #             for x , col in enumerate(row):
                
# #                 #for every direction
# #                 xval = x*self.xval
# #                 yval = y*self.yval
# #                 if y == posx and x == posy:

# #                     self.traversedlist[y][x] = 1
    
#     def PathFind(self,x,y):
#         xval = 1840//len(self.map[0])
#         yval = 1000//len(self.map)
#         xdist= self.rect.x - x
#         ydist = self.rect.y - y
#         #for y, 
        
        
        
#         #get the distance between the enemy and player
#         #in that distance check whether if in that path there is an obstacle 
        
#         pass
   
#     #we can parse in a obstacle object by default so that it can be accessed at any time, then based on the values of the obstacle size and center, the enemy can then move 
#     #away from the obstacle or try new paths to get to the enemy
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
    def __init__(self,screenx,screeny,size,colour):
        super().__init__(screenx,screeny,size,colour)
        self.health = 10
    # def update(self,x,y): #simple enemy movement to move to player

        
        
    #     xdist= self.rect.x - x
    #     ydist = self.rect.y - y
    #     #print(xdist,ydist)
        
        
        
    #     if xdist > 0:
    #         self.rect.x-=1
            
    #     elif xdist <0 :
    #         self.rect.x+=1
            
    #     elif  ydist>0:
    #         self.rect.y-=1
           
    #     elif  ydist<0:
    #         self.rect.y +=1
        
            
        