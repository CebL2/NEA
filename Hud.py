from tkinter import E
import pygame
pygame.init()
class Hud:  #WIP
    def __init__(self,screen,health =3):
        #healht bar are 3 squares
        self.screen = screen
        self.health = health
        self._Red = ((255,0,0))
        self._Black = ((0,0,0))
        self.Colour1 = self._Red
        self.Colour2 = self._Red
        self.Colour3 = self._Red
        
    def Health(self,Colour1,Colour2,Colour3):
        pass
    
    def DrawHealth(self):
        
        health_1 =pygame.draw.rect(self.screen,self.Colour1,(0,0,80,40))
        health_2 =pygame.draw.rect(self.screen,self.Colour2,(100,0,80,40))
        health_3 =pygame.draw.rect(self.screen,self.Colour3,(200,0,80,40))
    def update(self):
        
        if self.health == 3:
            pass
        elif self.health == 2:
            self.Colour3 = self._Black
        else:
            self.Colour3 = self._Black
            self.Colour2 = self._Black
        self.DrawHealth()
        #if self.health == 3:
            
        
    def Inventory(self):
        pass