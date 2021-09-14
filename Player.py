import pygame 


class Player(pygame.sprite.Sprite):
    player_image = pygame.image.load("spritegroup//test sprite.jpg").convert()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.center = (1280/2, 1024/2)
        self.spawnx = 200
        self.spawny = 200
        self.border = 2
            
    # def update(self):
    #     keypressed = pygame.key.get_pressed()
    #     if keypressed[pygame.K_s] and self.rect.y < screeny:
    #         self.rect.y += self.border
    #     if keypressed[pygame.K_a] and self.rect.x > self.border:
    #         self.rect.x -= self.border
    #     if keypressed[pygame.K_d] and self.rect.x <  screenx :
    #         self.rect.x += self.border
    #     if keypressed[pygame.K_w] and self.rect.y > self.border:
    #         self.rect.y -= self.border
    def moveright(self):
        self.rect.x += self.border
    def moveleft(self):
        self.rect.x -= self.border
    def moveup(self):
        self.rect.y -= self.border
    def movedown(self):
        self.rect.y += self.border
        
#def enemystate(collide)
# if collide is true:
#      enemystate is True
#      while enemystate is True:
#           colliding into walls will not teleport the player to the other side of the wall until enemystate becomes false again
#           the only way to do that is when the enemy count (or contents in the enemy list) is o
#           if enemycount == 0
#               enemystate = False

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
