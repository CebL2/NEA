
from Attack import *
import pygame 

class Player(pygame.sprite.Sprite):  #Player class
    player_image = pygame.Surface((50,50)) 
    player_image.fill((0,255,0))
    def __init__(self,screenx,screeny):      
        pygame.sprite.Sprite.__init__(self) 
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.center = (screenx/2, screeny/2)
        self.speed = 10 
        self.screenx = screenx
        self.screeny = screeny
        self.gap = 0 
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
        projectileup = Attack(self.rect.centerx,self.rect.centery-100,self.screenx,self.screeny,1)
        self.projectilegroup.add(projectileup)

    def Attackright(self):
        projectiledown = Attack(self.rect.centerx+50,self.rect.centery,self.screenx,self.screeny,2)
        self.projectilegroup.add(projectiledown)
        
    def Attackleft(self):
        projectiledown = Attack(self.rect.centerx-50,self.rect.centery,self.screenx,self.screeny,3)
        self.projectilegroup.add(projectiledown)
        
    def Attackdown(self):
        projectiledown = Attack(self.rect.centerx,self.rect.centery+100,self.screenx,self.screeny,4)
        self.projectilegroup.add(projectiledown)
        

# def characterCreation():
#     while running:
#         screen.fill(White)
#         screen.blit(textfont.render("Choose your class"))
#         right = pygame.draw.rect(screen, Black,(300,300,100,100))
#         c = textfont.render("Warrior", True, White), (50,50)
#         screen.blit(c)
#         mousex, mousey = pygame.mouse.get_pos()
#         if right.collidepoint(mousex,mousey):
#             c = textfont.render("Mage",True,White),(50,50)
#             screen.blit(c,(50,50))
#         if right.collidepoint(mousex,mousey):
#             c = textfont.render("Warrior",True,White)    
