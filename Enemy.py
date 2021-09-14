import pygame, random

class Enemy(pygame.sprite.Sprite):
    enemy  = pygame.image.load("spritegroup//test enemy.png").convert()
    def __init__(self,enemy,enemylist):
        pygame.sprite.Sprite.__init__(self)
        self.enemy = enemy
        self.image = Enemy.enemy
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)       
        self.enemylist = enemylist
        #self.screen = screen
        #self.spritegroup = spritegroup
        #self.spritegroup.add()
        
        #lets make the enemy spawn a list       
    def SpawnEnemy(self,difficulty): 
        if difficulty == 0:
            return None
        if difficulty == 1:
            for i in range(0,2):
                self.enemyposition = (random.randint(20,1000), random.randint(20,1000))
                self.enemylist.append(self.enemyposition)
                #self.enemylist.append(self.enemyposition()#[(100,200), (300,1000)]
            for position in self.enemylist:
                self.rect.center = (position[0],position[1])
                    #screen.fill(White)
                
    
    #if difficulty == 2:
    #    for i in range( pawnamount_medium):
    #        screen.blit(textfont.render(enemy, True, Black ), (random.randint(0,1280),random.randint(0,1080)))
    #else:
     #   for i in range(spawnamount_hard): 
      #      screen.blit(textfont.render(enemy, True, Black ), (random.randint(0,1280),random.randint(0,1080)))

#TODO