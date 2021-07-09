import pygame
import os

pygame.mixer.init()

#sound
def playMusic():
    pygame.mixer.music.load(os.path.join("assets","SuperMarioBros.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def pauseMusic():
    pygame.mixer.music.stop()

def playJumpSound():
    jumpSound=pygame.mixer.Sound(os.path.join("assets","jump.wav"))
    pygame.mixer.Sound.play(jumpSound)

def playCoinSound():
    coinSound=pygame.mixer.Sound(os.path.join("assets","coin.wav"))
    pygame.mixer.Sound.play(coinSound)

def playKickSound():
    kickSound=pygame.mixer.Sound(os.path.join("assets","kick.wav"))
    pygame.mixer.Sound.play(kickSound)

def playLooseSound():
    dieSound=pygame.mixer.Sound(os.path.join("assets","MarioDie.wav"))
    pygame.mixer.Sound.play(dieSound)