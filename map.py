import pygame
import tileID
import tile
import coin

mapArray=[
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,5,0,0,0,0,4,4,4,0,0,5,0,0,0,0,0,0,0,0,0,0,
1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1
]

tileArray=[]

arrayPosX=0
arrayPosY=0


for i in range(len(mapArray)):
    if mapArray[i]==1:
        tileObject=tile.Tile(tileID.groundBlock)
        tileObject.rect.x=(16*arrayPosX)
        tileObject.rect.y=(16*arrayPosY)
        tileArray.append({"id":"1","data":tileObject})
    if mapArray[i]==2:
        tileObject=tile.Tile(tileID.supriseBlock)
        tileObject.rect.x=(16*arrayPosX)
        tileObject.rect.y=(16*arrayPosY)
        tileArray.append({"id":"2","data":tileObject})
    if mapArray[i]==3:
        tileObject=tile.Tile(tileID.floatingBlock)
        tileObject.rect.x=(16*arrayPosX)
        tileObject.rect.y=(16*arrayPosY)
        tileArray.append({"id":"3","data":tileObject})
    if mapArray[i]==4:
        tileObject=tile.Tile(tileID.obstacleBlock)
        tileObject.rect.x=(16*arrayPosX)
        tileObject.rect.y=(16*arrayPosY)
        tileArray.append({"id":"4","data":tileObject})
    if mapArray[i]==5:
        tileObject=tile.Tile(tileID.pipes)
        tileObject.rect.x=(16*arrayPosX)
        tileObject.rect.y=(16*arrayPosY)-16##move the yPos slightly up
        tileArray.append({"id":"5","data":tileObject})

    arrayPosX+=1
    if arrayPosX>29:
        arrayPosY+=1
        arrayPosX=0

