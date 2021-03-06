import pygame
pygame.init()
class HealthBar:  #WIP
    def __init__(self,screen,health =3):
        self.screen = screen
        self.health = health
        self._Red = ((255,0,0))
        self._Black = ((0,0,0))
        self.Colour1 = self._Red
        self.Colour2 = self._Red
        self.Colour3 = self._Red

    def DrawHealth(self):
        health_1 =pygame.draw.rect(self.screen,self.Colour1,(0,0,80,40)) #draws the health bars
        health_2 =pygame.draw.rect(self.screen,self.Colour2,(100,0,80,40))
        health_3 =pygame.draw.rect(self.screen,self.Colour3,(200,0,80,40))
        
    def update(self):
     
        if self.health == 3: #depending on the health of the player, the colour of the health bars will be black, meaning that the player has lost some health
            pass 
        elif self.health == 2:
            self.Colour3 = self._Black
        else:
            self.Colour3 = self._Black
            self.Colour2 = self._Black
        self.DrawHealth()


class MiniMap():
    def __init__(self,screen,maplist,traversed=None):   
        self.map = maplist  #a passed in map or array 
        self.image = pygame.Surface((300,150)) #the background of the minimap
        self.backgroundcolour = (200,200,200)
        self.Black = (0,0,0)
        self.xval = self.image.get_width()//len(self.map[0]) #takes the width and height of the image and divided by the width and height of the map respectively
        self.yval = self.image.get_height()//len(self.map) #this would give us the size of each room in the minimap
        self.green = (0,255,0)
        self.gray = (220,220,220)
        self.yellow =(255,255,0)
        self.red = (255,0,0)
        self.screen = screen
        self.image.fill(self.backgroundcolour)
        if traversed == None:
            self.traversedlist = self.traversed()
        else:
            self.traversedlist = traversed
    def isBorder(self,i, i_length, j, j_length): #checks if the list element is on the border
        if i == 0 or i == i_length or j== 0 or j == j_length:
            return True

    def isCorner(self,i, i_length, j, j_length):
        if i == 0 and j == 0 or i == 0 and j == j_length or i == i_length and j == 0 or i == i_length and j == j_length: #checks if the list element is on the corner
            return True 
    def traversed(self):
        traversedlist = []  #makes an empty array if there isn't a array passed in from the class to begin with
        for i in range(0,len(self.map)):
            traversedlist.append([])
            for _ in range(0,len(self.map[0])):
                traversedlist[i].append(0)
        return traversedlist
    def drawgrid(self,posx,posy):
        for y, row in enumerate(self.map):  #element, value
            for x , col in enumerate(row):
                xpos = x*self.xval
                ypos = y*self.yval
                if y == posx and x == posy:
                    self.traversedlist[y][x] = 1  
                Directionlist = [(0,1),(0,-1),(1,0),(-1,0)] #similar operations with how the layout of the map was generated, but instead it is used to determine which room has been traversed
                if self.isBorder(y,len(self.map)-1,x,len(self.map[0])-1):
                    if self.isCorner(y,len(self.map)-1,x,len(self.map[0])-1):
                        if y == 0 and x == 0:  #top left corner
                            #remove left and up
                            Directionlist.remove((0,-1))
                            Directionlist.remove((-1,0))
                        elif y == 0 and x == len(self.map[0])-1: #top right corner
                            #remove right and up
                            Directionlist.remove((0,1))
                            Directionlist.remove((-1,0))
                        elif y == len(self.map)-1 and x == len(self.map[0])-1: #button right corner
                            #remove down and right
                            Directionlist.remove((0,1))
                            Directionlist.remove((1,0))
                        elif y == len(self.map)-1 and x == 0: #bottom left corner
                            #remove left and down
                            Directionlist.remove((0,-1))
                            Directionlist.remove((1,0))
                    else:
                        if y == 0:  #top 
                            #remove up
                            Directionlist.remove((-1,0))
                        elif y == len(self.map)-1: #bottom
                            #remove down
                            Directionlist.remove((1,0))
                        elif x == 0: #left
                            #remove left
                            Directionlist.remove((0,-1))
                        else: #right 
                            #remove right
                            Directionlist.remove((0,1))  
                rect = pygame.Rect(1582.5+xpos,39+ypos,self.xval-4,self.yval-4) #preset rect to be drawn
                pygame.draw.rect(self.screen,self.Black,rect)  #by default, all rooms are black

                if self.map[y][x] == 'B' or self.map[y][x] == 'E' or self.map[y][x] == 'R':      #if the current position of the map is NOT where the player is currently
                    for direction in Directionlist:
                        if self.map[y+direction[0]][x+direction[1]] == '#': #and the neighbouring room is where the player is 
                            self.traversedlist[y][x] = 1 #then make that position in the traversedlist equal to 1
                if self.traversedlist[y][x] >0: #if the current position of the traversedlist is greater than 0, then the rectangle drawn in that specific location will be gray instead of black
                    pygame.draw.rect(self.screen,self.gray,rect)
                if self.map[y][x] == '#':
                    pygame.draw.rect(self.screen,self.green,rect) #otherwise, if the position is where the player is, then colour the rectangle green
           
    def update(self,x,y):
        self.drawgrid(x,y)
        self.screen.blit(self.image,(1580,39)) #projects the background of the minimap
        
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_m]:
        
            self.image.set_alpha(100) #minimap by default would be slightly less visible if a key is not pressed, in this case, while the key 'M' is pressed down, the minimap will be 
        else:                         #a bit more visible by making the background of the minimap more transparent
            
            self.image.set_alpha(200)
    
        
