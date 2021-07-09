from typing import Counter
import pygame
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self,xPos=170,yPos=210):
        super().__init__()
        self.image=pygame.image.load(os.path.join("assets","enemies.png"))
        self.subsurfaceImage=pygame.Surface.subsurface(self.image,(0,19,18,18))
        self.mask=pygame.mask.from_surface(self.subsurfaceImage)
        self.rect=pygame.mask.Mask.get_rect(self.mask)

        self.rect.x=xPos
        self.rect.y=yPos

        self.velocity=1
        self.counter=0

        self.alive=True

    def render(self,screen):
        #simple enemy behaviour
        self.rect.x+=self.velocity
        self.counter+=1
        if self.counter>=45:
            self.velocity=-self.velocity
            self.counter=0

        if self.alive==True:
            screen.blit(self.subsurfaceImage,(self.rect.x,self.rect.y))