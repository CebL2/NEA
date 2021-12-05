import pygame, random

screenx = 1920
screeny = 1080
screen = pygame.display.set_mode((screenx,screeny))
class Enemy(pygame.sprite.Sprite):
    Enemy  = pygame.Surface((200,200)) #pygame.image.load("spritegroup//test enemy.png").convert()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.playerx = 1
        self.playery = 1
        self.image = Enemy.Enemy
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(0,1280),(random.randint(0,1024))))   
        self.x = self.rect.x
        self.y = self.rect.y 
        self.health = 2
        self.speed = 1
        
        
    def killSprite(self):
        if self.health == 0:
            self.kill()
        else:
            return 0 
    def update(self):
        
        pass
        #enemy AI
        #get position of the player center x and y
        #default is to run towards the player if its melee
        #if enemy is ranged, consider staying a distance and shooting the player
        #and if the player comes close, then the enemy will try and run away in a direction
        #
        
    
    
    
        #self.screen = screen
        #self.spritegroup = spritegroup
        #self.spritegroup.add()
        
        #lets make the enemy spawn a list       
    # def SpawnEnemy(self,difficulty): 
    #     x = 0
    #     y = 0
    #     if difficulty == 0:
    #         return None
    #     if difficulty == 1:
    #         for i in range(3):
    #             self.enemyposition = (random.randint(20,1000), random.randint(20,1000))
    #             self.enemylist.append(self.enemyposition)
    #             self.enemylist.append(self.enemyposition()#[(100,200), (300,1000)]
    #         for enemy in self.enemylist:
    #             x = enemy[0] 
    #             y = enemy[1]
              
                #screen.blit(self.image,(x,y))
                    
                    #screen.fill(White)
        
    def MoveToPlayer(self):  
        pass
    #if difficulty == 2:
    #    for i in range( pawnamount_medium):
    #        screen.blit(textfont.render(enemy, True, Black ), (random.randint(0,1280),random.randint(0,1080)))
    #else:
     #   for i in range(spawnamount_hard): 
      #      screen.blit(textfont.render(enemy, True, Black ), (random.randint(0,1280),random.randint(0,1080)))

#TODO
# enemies = pygame.sprite.Group()
# enemy = Enemy()
# for i in range(0,3):
#     enemies.add(enemy)
    
# print(enemies.sprites())

#print(enemy.enemylist)
#enemies.add(enemy.enemylist)  

