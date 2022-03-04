import pygame
pygame.init()
class Hud:  #WIP
    def __init__(self,screen):
        #healht bar are 3 squares
        self.screen = screen
        self.health = 3
        # self._Red = ((255,0,0))
        # self._Black = ((0,0,0))
        self._Colour = None
        
    def update(self):
        health_1 =pygame.draw.rect(self.screen,self._Colour,(0,0,80,50))
        health_2 =pygame.draw.rect(self.screen,self._Colour,(100,0,80,50))
        health_3 =pygame.draw.rect(self.screen,self._Colour,(200,0,80,50))
        

    def Inventory(self):
        pass