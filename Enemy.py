from this import d
import pygame, random
import numpy as np
#from NEAMain import *
#import NEAMAIN

#x = screenx
#print(x)
#screen = pygame.display.set_mode((screenx,screeny))
class Enemy(pygame.sprite.Sprite):
    Enemy  = pygame.Surface((200,200)) #pygame.image.load("spritegroup//test enemy.png").convert()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Game.__init__(self)
        #self.ad = Game.screenx
        #Game.__init__(self)
        self.playerx = 1
        self.playery = 1
        self.image = Enemy.Enemy
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(0,1280),(random.randint(0,1024))))   
        self.health = 2
        self.speed = 1
        #self.x = Game.screenx
        #self.y = Game.screeny
  #

    def killSprite(self):
        if self.health == 0:
            self.kill()
        else:
            return 0 
    #consistently update player position in a different class 
   # def GetPlayerPos(self):
        
    #    return(self.playerx, self.playery)

     #   self.GetPlayerPos()
        
    #def FollowPlayerpos(self,x,y):
        
           # self.FollowPlayerpos(x,y)
   
        
    def update(self,x,y):
        #playerpos = 
        
        #player position has to be constantly updated, this is just getting one instance 
        #distancex = self.playerx - self.rect.x
        #distancey = self.playery - self.rect.y
        #print(self.)
        #print(distancex,distancey)
        #print(x,y)
        xdist= self.rect.x - x
        ydist = self.rect.y - y
        print(xdist,ydist)
        if xdist > 0:
            self.rect.x-=1
            #self.rect.y-=1
            #self.FollowPlayerpos(x,y)
        elif xdist <0 :#and ydist>0:
            self.rect.x+=1
            #self.rect.y-=1
           # self.FollowPlayerpos(x,y)
        elif  ydist>0:
            #self.rect.x-=1
            self.rect.y-=1
            #self.FollowPlayerpos(x,y)
        elif  ydist<0:
          #  self.rect.x +=1
            self.rect.y +=1
      #  pass
       ## print(self.ad)
        #print(self.x,self.y)
        
            
        # probup = 0.25
        # probdown = 0.25
        # probleft = 0.25
        # probright = 0.25
        # directions = ['up','down','left','right']
        # RoomDirection = np.random.choice(directions,p=[probup,probdown,probleft,probright])
        # if RoomDirection == 'up':
        #     self.rect.y -=1
        # if RoomDirection == 'down':
        #     self.rect.y +=1
        # if RoomDirection == 'right':
        #     self.rect.x +=1
        # if RoomDirection == 'left':
        #     self.rect.x -=1
           
        
       # pass
       
            
        #self.MoveToPlayer(self.playerx,self.playery)
        #enemy AI
        #get position of the player center x and y
        #default is to run towards the player if its melee
        #if enemy is ranged, consider staying a distance and shooting the player
        #and if the player comes close, then the enemy will try and run away in a direction
        #
        
    
    
        
    def MoveToPlayer(self):
        
        #while self.playerx!= self.rect.x and self.playery !=self.rect.y:
        
        pass
       
              
        
   
# enemies = pygame.sprite.Group()
# enemy = Enemy()
# for i in range(0,3):
#     enemies.add(enemy)
    
# print(enemies.sprites())

#print(enemy.enemylist)
#enemies.add(enemy.enemylist)  

