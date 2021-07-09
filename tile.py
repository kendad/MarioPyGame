import pygame
import os

class Tile(pygame.sprite.Sprite):
    def __init__(self,tileSheetPosition):
        super().__init__()
        self.tileSheetPosition=tileSheetPosition#(x,y,w,h)
        self.image=pygame.image.load(os.path.join("assets","blocks.png"))
        self.subsurfaceImage=pygame.Surface.subsurface(self.image,self.tileSheetPosition)
        self.image=self.subsurfaceImage
        #self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=pygame.mask.Mask.get_rect(self.mask)
    
    def render(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))