from Attack import * #imports the attack module from local files
import random
import pygame 


class Unit(pygame.sprite.Sprite): 
    '''
    general unit class to be used for other objects, since all units are sprites, the class must inherit the sprite class from pygame
    '''
    def __init__(self,screenx,screeny,size,colour):
        super().__init__() #initialises the sprite object to access and assign variables
        self.screenx = screenx #
        self.screeny = screeny
        self.image = pygame.Surface(size) #creates a image of the size given
        self.image.fill(colour) #and fills it with the colour passed through the class
        self.rect = self.image.get_rect() #gets the rectangle object
        self.projectilegroup = pygame.sprite.Group() 
    
    def Attack(self,direction):  #attack functions for projectiles
        projectileup = Attack(self.rect.centerx,self.rect.centery,self.screenx,self.screeny,direction)
        self.projectilegroup.add(projectileup)
    

class Player(Unit): 
    '''
    Player class
    '''
    def __init__(self,screenx,screeny,size,colour,centerx= None,centery= None):   #screen values are passed in  
        self.centerx = centerx
        self.centery = centery
        super().__init__(screenx,screeny,size,colour) #initiliases the unit class with it's own values8
        if self.centerx == None: #if either of the center of the player's position is None
            self.rect.center = (self.screenx/2, self.screeny/2) #then by default, the player is at the center of the screen
        else:
            self.rect.center = (self.centerx, self.centery) #otherwise, the center is the value of what was passed in
        self.state = 1 #vulnerable state is 1, if the player is hit, state changes to 0 for 1.5 seconds before turning back into 1
        self.speed = 10 
            
    def Movement(self):
        '''
        Player movement based on input keys
        '''
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_s] and self.rect.y < self.screeny: 
            self.rect.y += self.speed
        if keypressed[pygame.K_w] and self.rect.y > 0:
            self.rect.y  -= self.speed
        if keypressed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keypressed[pygame.K_d] and self.rect.x <  self.screenx:
            self.rect.x += self.speed
    def update(self,obstaclegroup):  #update function to move player
        self.Movement()
        for obs in obstaclegroup: 
            if self.rect.colliderect(obs.rect): #if the player collides with the obstacle
                if self.rect.y+40 > obs.rect.y and self.rect.y+10 < obs.rect.y+obs.ysize: #and player collides at either left or right side of the obstacle 
                    if obs.rect.collidepoint(self.rect.x,self.rect.y) or obs.rect.collidepoint(self.rect.x,self.rect.y+50): #check if the top left and bottom left corners of the player has collided
                        self.rect.x = obs.rect.x+obs.xsize #if collided, then the player remains the same where it collided, in this case, right of the obstacle
                    elif obs.rect.collidepoint(self.rect.x+50,self.rect.y) or obs.rect.collidepoint(self.rect.x+50,self.rect.y+50): #if the top right and bottom right corners collide
                        self.rect.x= obs.rect.x-50 #then the player stays at the left size of the obstacle   
                else:  #similar process, but for the bottom and top parts of the obstacle
                    if obs.rect.collidepoint(self.rect.x,self.rect.y+50) or obs.rect.collidepoint(self.rect.x+50,self.rect.y+50):
                        self.rect.y = obs.rect.y-50
                    elif  obs.rect.collidepoint(self.rect.x,self.rect.y) or obs.rect.collidepoint(self.rect.x+50,self.rect.y):
                        self.rect.y = obs.rect.y+obs.ysize
            for projectile in self.projectilegroup: #goes through each projectile in the projectile group of the player
                if pygame.sprite.spritecollideany(projectile,obstaclegroup):  #if any of the existing projectiles collide with any of the obstacles
                    projectile.kill()  #destroy the projectile


class Enemy(Unit):
    def __init__(self,screenx,screeny,size,colour):
        '''
        Enemy class
        '''
        super().__init__(screenx,screeny,size,colour)
        self.rect.center = ((random.randint(500,1000),(random.randint(300,900))))   
        self.health = random.randint(1,5)
        self.speed = 1
        

    def update(self,x,y,obstaclegroup): 
        '''
        Movement to follow player based on player position on the screen and obstacle collision
        '''
        for obs in obstaclegroup: 
            if self.rect.colliderect(obs.rect):  #colliderect  = true
                if self.rect.y+45 > obs.rect.y and self.rect.y+10 < obs.rect.y+obs.ysize: 
                    if obs.rect.collidepoint(self.rect.x,self.rect.y) or obs.rect.collidepoint(self.rect.x,self.rect.y+100): #left colilde
                        self.rect.x = obs.rect.x+obs.xsize
                    elif obs.rect.collidepoint(self.rect.x+100,self.rect.y) or obs.rect.collidepoint(self.rect.x+100,self.rect.y+100): #right collide
                        self.rect.x= obs.rect.x-100
                else:
                    if obs.rect.collidepoint(self.rect.x,self.rect.y+100) or obs.rect.collidepoint(self.rect.x+100,self.rect.y+100):
                        self.rect.y = obs.rect.y-100
                    elif  obs.rect.collidepoint(self.rect.x,self.rect.y) or obs.rect.collidepoint(self.rect.x+100,self.rect.y):
                        self.rect.y = obs.rect.y+obs.ysize
            else:
                if self.rect.centerx < x:
                    self.rect.x += self.speed
                elif self.rect.centerx > x:
                    self.rect.x -= self.speed
                if self.rect.centery < y:
                    self.rect.y +=  self.speed
                elif self.rect.centery > y:
                    self.rect.y -= self.speed
              


'''
Types of enemies that could spawn
'''
class MeleeEnemy(Enemy):
    def __init__(self,screenx,screeny,size,colour):
        super().__init__(screenx,screeny,size,colour)
        self.state = 0
        
 
class RangedEnemy(Enemy):
    def __init__(self,screenx,screeny,size,colour):
        super().__init__(screenx,screeny,size,colour)
        self.state = 1
        self.cooldown = 0
        
class Boss(RangedEnemy):
    def __init__(self,screenx,screeny,size,colour):
        super().__init__(screenx,screeny,size,colour)
        self.health = 10
      