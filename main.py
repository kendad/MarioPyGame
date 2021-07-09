import pygame
import map
import player
import coin
import enemy
import sound

SCREEN_WIDTH=300#300#LEVEL_WIDTH=480
SCREEN_HEIGHT=240

pygame.init()
clock=pygame.time.Clock()
gameState="NEUTRAL"

tileArray=map.tileArray
mapVelocity=2

mario=player.Player()
time_interval=100
last_update=0

mainCoin=coin.Coin(0,4)
mainCoin.activate=True

#coin values are hard coded
coin1=coin.Coin(50,82)
coin2=coin.Coin(98,82)
coin3=coin.Coin(305,45)
coin1Activate=True
coin2Activate=True
coin3Activate=True

enemy=enemy.Enemy()

#sound
sound.playMusic()


screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Mario 1-1")

isGameRunning=True

while isGameRunning:
    
    marioDirection="idle"
    keyPressed=pygame.key.get_pressed()
    if keyPressed[pygame.K_RIGHT]:
        marioDirection="right"
    if keyPressed[pygame.K_LEFT]:
        marioDirection="left"
    if keyPressed[pygame.K_SPACE]:
        marioDirection="up"   
    
    #plays mario related sound
    if marioDirection=="up":
        sound.playJumpSound()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isGameRunning=False
            
    
    screen.fill((135,206,235))

    #moves the map-->camera
    if marioDirection=="right":
        for item in tileArray:
            item["data"].rect.x-=mapVelocity
        coin1.rect.x-=mapVelocity
        coin2.rect.x-=mapVelocity
        coin3.rect.x-=mapVelocity
        enemy.rect.x-=mapVelocity
    
    if marioDirection=="left":
        for item in tileArray:
            item["data"].rect.x+=mapVelocity
        coin1.rect.x+=mapVelocity
        coin2.rect.x+=mapVelocity
        coin3.rect.x+=mapVelocity
        enemy.rect.x+=mapVelocity


    #detects collison between object
    for i in range(len(tileArray)):
        if pygame.sprite.collide_mask(mario,tileArray[i]["data"]):
            if tileArray[i]["id"]=="1":
                mario.gravity=0
                mario.velocity=100
                mario.rect.bottom=tileArray[i]["data"].rect.top
            #suprise Blocks
            #hits the bottom of the block
            if tileArray[i]["id"]=="2" and mario.rect.top<=tileArray[i]["data"].rect.bottom:
                tileArray[i]['data'].rect.y=100
                mario.velocity=100#means i can jump again
                #hard coded coin activation
                if i==4:
                    coin1.activate=coin1Activate
                if i==7:
                    coin2.activate=coin2Activate
                if i==0:
                    coin3.activate=coin3Activate
            #hits the top of the block
            if tileArray[i]["id"]=="2" and mario.rect.bottom>=tileArray[i]["data"].rect.top and mario.rect.top<tileArray[i]["data"].rect.top:
                mario.rect.bottom=tileArray[i]["data"].rect.top
            #floatingBlocks
            if tileArray[i]["id"]=="3" and mario.rect.top<=tileArray[i]["data"].rect.bottom:
                mario.velocity=0
            if tileArray[i]["id"]=="3" and mario.rect.bottom>=tileArray[i]["data"].rect.top and mario.rect.top<tileArray[i]["data"].rect.top:
                mario.rect.bottom=tileArray[i]["data"].rect.top
                mario.velocity=100
            #pipes
            if tileArray[i]["id"]=="5" and mario.rect.bottom>=tileArray[i]["data"].rect.top:
                mario.rect.bottom=tileArray[i]["data"].rect.top
                mario.velocity=100
            #obstacleBlock
            if tileArray[i]["id"]=="4" and mario.rect.bottom>=tileArray[i]["data"].rect.top:
                mario.rect.bottom=tileArray[i]["data"].rect.top
                mario.velocity=100

        else:
            mario.gravity=5

    if pygame.time.get_ticks()-last_update>time_interval:
        mario.animate(marioDirection)
        last_update=pygame.time.get_ticks() 
    
    for item in tileArray:#renders the map
        item["data"].render(screen)
    mario.render(screen)
    
    mainCoin.render(screen)
    coin1.render(screen)
    coin2.render(screen)
    coin3.render(screen)
    if pygame.sprite.collide_mask(mario,coin1) and coin1.activate==True:
        sound.playCoinSound()
        mario.score+=1
        coin1Activate=False
        coin1.activate=False
    if pygame.sprite.collide_mask(mario,coin2) and coin2.activate==True:
        sound.playCoinSound()
        mario.score+=1
        coin2Activate=False
        coin2.activate=False
    if pygame.sprite.collide_mask(mario,coin3) and coin3.activate==True:
        sound.playCoinSound()
        mario.score+=1
        coin3Activate=False
        coin3.activate=False

    enemy.render(screen)
    if pygame.sprite.collide_mask(mario,enemy):
        if enemy.alive==True:
            sound.playKickSound()
        enemy.alive=False

    if mario.rect.y>SCREEN_HEIGHT:
        pygame.quit()

    pygame.display.update()
    clock.tick(60)
