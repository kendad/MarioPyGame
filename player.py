import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imageFrameStart=0
        self.imageFrameLimiter=0

        self.image=pygame.image.load(os.path.join("assets","mario.png"))
        self.subsurfaceImage=pygame.Surface.subsurface(self.image,(self.imageFrameStart,0,18,36))
        
        #self.rect=self.subsurfaceImage.get_rect()
        self.mask=pygame.mask.from_surface(self.subsurfaceImage)
        self.rect=pygame.mask.Mask.get_rect(self.mask)
        self.rect.x=200

        self.direction="right"
        self.gravity=5
        self.velocity=200

        self.score=0

        pygame.font.init()
        self.myfont=pygame.font.SysFont("Comic Sans MS",18)
    
    def render(self,screen):
        self.rect.y+=self.gravity
        self.renderScore(screen)
        screen.blit(self.subsurfaceImage,(self.rect.x,self.rect.y))
    
    def animate(self,direction):
        if direction=="right":
            self.direction="right"
            self.imageFrameStart+=18
            if self.imageFrameStart>=126:
                self.imageFrameStart=72
            self.subsurfaceImage=pygame.Surface.subsurface(self.image,(self.imageFrameStart,0,18,36))
        if direction=="left":
            self.direction="left"
            self.imageFrameStart+=18
            if self.imageFrameStart>=126:
                self.imageFrameStart=72
            self.subsurfaceImage=pygame.Surface.subsurface(self.image,(self.imageFrameStart,0,18,36))    
            self.subsurfaceImage=pygame.transform.flip(self.subsurfaceImage,True,False)
            
        if direction=="idle":
            self.imageFrameStart=0
            self.subsurfaceImage=pygame.Surface.subsurface(self.image,(self.imageFrameStart,0,18,36))
            if self.direction=="left":
                self.subsurfaceImage=pygame.transform.flip(self.subsurfaceImage,True,False)
        
        if direction=="up":
            self.rect.y-=self.velocity
            if self.rect.y<=20:
                self.velocity=0
            self.imageFrameStart=36
            self.subsurfaceImage=pygame.Surface.subsurface(self.image,(self.imageFrameStart,0,18,36))
            if self.direction=="left":
                self.subsurfaceImage=pygame.transform.flip(self.subsurfaceImage,True,False)

    def renderScore(self,screen):
        textsurface=self.myfont.render(str(self.score),False,(0,0,0))
        screen.blit(textsurface,(25,0))

