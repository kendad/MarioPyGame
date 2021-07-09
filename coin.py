import pygame
import os

class Coin(pygame.sprite.Sprite):
    def __init__(self,xPos=0,yPos=0):
        super().__init__()
        self.frame=146
        self.image=pygame.image.load(os.path.join("assets","blocks.png"))
        self.subsurfaceImage=pygame.Surface.subsurface(self.image,(self.frame,176,12,16))
        self.mask=pygame.mask.from_surface(self.subsurfaceImage)
        self.rect=pygame.mask.Mask.get_rect(self.mask)

        self.rect.x=xPos
        self.rect.y=yPos

        self.activate=False
    
    def render(self,screen):
        if self.activate==True:
            screen.blit(self.subsurfaceImage,(self.rect.x,self.rect.y))