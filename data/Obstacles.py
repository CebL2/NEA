import pygame, random
class RoomObstacles(pygame.sprite.Sprite):
    def __init__(self,i,j,bosspos = None,xsize=None,ysize=None,xcenter=None,ycenter = None): #map indexes
        super().__init__()
        self.i = i
        self.j = j
        self.BossPos = bosspos
        self.randomchoice = random.randint(1,2) #random values to assign positions to where the obstacles can spawn
        self.randomxcenter1 = random.randint(300,800)   
        self.randomxcenter2 = random.randint(1000,1500)
        self.randomycenter1 = random.randint(300,400)
        self.randomycenter2 = random.randint(500,700)
         
        if self.BossPos == (self.i,self.j):
            self.randomxcenter1 = random.randint(300,500) #manipulate where the obstacles and be put to make sure it does not cover the exit to the next level
            self.randomxcenter2 = random.randint(1200,1500)
            self.randomycenter1 = random.randint(300,400)
            self.randomycenter2 = random.randint(800,900)
       
        if xsize == None:
            if self.randomchoice ==1: 
                self.xsize = random.randint(100,200) #two random selection of sizes are to be chosen from to add a bit of variety
                self.ysize= random.randint(100,300)
                self.xcenter=self.randomxcenter1
                self.ycenter= self.randomycenter1
            else:
                self.xsize = random.randint(100,300)
                self.ysize= random.randint(50,300)
                self.xcenter=self.randomxcenter2
                self.ycenter= self.randomycenter2
        else:
            self.xsize = xsize
            self.ysize= ysize
            self.xcenter= xcenter
            self.ycenter=  ycenter
        self.image = pygame.Surface((self.xsize,self.ysize))
        self.image.fill((128,128,128))
        self.rect = self.image.get_rect()
        self.rect.center = (self.xcenter,self.ycenter)  


