import pygame, random

screenx = 1280
screeny = 1024
screen = pygame.display.set_mode((screenx,screeny))
class Enemy(pygame.sprite.Sprite):
    enemy  = pygame.Surface((200,200)) #pygame.image.load("spritegroup//test enemy.png").convert()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Enemy.enemy
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(0,1280),(random.randint(0,1024))))   
        self.x = self.rect.x
        self.y = self.rect.y 
    
        
    
    def update(self):
        
        pass
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

