import pygame
import random
x,y=0,0
screen=pygame.display.set_mode((600,600))
spriteR=pygame.image.load('Test\\SpriteR0.png').convert()
spriteU=pygame.image.load('Test\\SpriteU0.png').convert()
spriteD=pygame.image.load('Test\\SpriteD0.png').convert()
spriteL=pygame.image.load('Test\\SpriteL0.png').convert()
level0Night=pygame.image.load('level0Night.png').convert()
level0=pygame.image.load('level0.png').convert()
level1=pygame.image.load('level1.png').convert()
dId=pygame.image.load('Dude\\dudeidle.png').convert()
dR=pygame.image.load('Dude\\dudewalking.png').convert()
dR1=pygame.image.load('Dude\\dudewalking1.png').convert()
dL=pygame.image.load('Dude\\dudewalkingleft.png').convert()
dL1=pygame.image.load('Dude\\dudewalkingleft1.png').convert()
dIdL=pygame.image.load('Dude\\dudeidleleft.png').convert()
rainSprite=pygame.image.load('Rain.png').convert()
nightShader=pygame.image.load('night.png').convert_alpha()
scary=pygame.image.load('scary.png').convert()
nightShader.set_alpha(0)
scary.set_colorkey((0,0,0))
dId.set_colorkey((0,0,0))
dR.set_colorkey((0,0,0))
dR1.set_colorkey((0,0,0))
dL.set_colorkey((0,0,0))
dL1.set_colorkey((0,0,0))
dIdL.set_colorkey((0,0,0))
rainSprite.set_colorkey((0,0,0))
lastKey='right'
Rvalue=0
Lvalue=0
darkness=0
clock=pygame.time.Clock()
level=level0
scaryX=random.choice(range(50,550))
scaryY=random.choice(range(50,550))
ry=0
def moveRight():
    moveList=[dR,dR,dR,dR,dR,dR1,dR1,dR1,dR1,dR1]
    global Rvalue,curentSprite,clock
    clock.tick(60)
    curentSprite=moveList[Rvalue]
    Rvalue+=1
    if Rvalue>=len(moveList):
        Rvalue=0
def moveLeft():
    moveList=[dL,dL,dL,dL,dL,dL1,dL1,dL1,dL1,dL1]
    global Lvalue,curentSprite,clock
    clock.tick(60)
    curentSprite=moveList[Lvalue]
    Lvalue+=1
    if Lvalue>=len(moveList):
        Lvalue=0
curentSprite=dId
logo=pygame.image.load('LOGOUP.png').convert()
screen.blit(curentSprite,(x,y))
ran=0
lightRange=20
light=pygame.image.load('circle.png').convert()
def Light():
    nx=list(range(lightRange))
    ny=list(range(lightRange))
    if darkness>=210:
        for i in range(lightRange):
            itemx=random.choice(range(len(nx)))
            itemy=random.choice(range(len(ny)))
            nightShader.set_at((x+nx[itemx],y+ny[itemy]),(0,0,0,0))
            nx.pop(itemx)
            ny.pop(itemy)
        nx=list(range(lightRange))
        ny=list(range(lightRange))
        for i in range (lightRange):
            itemx=random.choice(range(len(nx)))
            itemy=random.choice(range(len(ny)))
            nightShader.set_at((x-nx[itemx],y-ny[itemy]),(0,0,0,0))
            nx.pop(itemx)
            ny.pop(itemy)
        nx=list(range(lightRange))
        ny=list(range(lightRange))
        for i in range (lightRange):
            itemx=random.choice(range(len(nx)))
            itemy=random.choice(range(len(ny)))
            nightShader.set_at((x-nx[itemx],y+ny[itemy]),(0,0,0,0))
            nx.pop(itemx)
            ny.pop(itemy)
        nx=list(range(lightRange))
        ny=list(range(lightRange))
        for i in range (lightRange):
            itemx=random.choice(range(len(nx)))
            itemy=random.choice(range(len(ny)))
            nightShader.set_at((x+nx[itemx],y-ny[itemy]),(0,0,0,0))
            nx.pop(itemx)
            ny.pop(itemy)
def unLight():
    #nx=list(range(600))
    #ny=list(range(600))
    #if darkness>=210:
    #    for i in range(600):
    #        itemx=random.choice(range(len(nx)))
    #        itemy=random.choice(range(len(ny)))
    #        nightShader.set_at((nx[itemx],ny[itemy]),(0,0,0,255))
    #        nx.pop(itemx)
    #        ny.pop(itemy)
    nightShader.fill('black')
        
        
        
print(nightShader.get_at((x,y)))
nightShader.set_at((x,y),(255,0,0,170))
Light()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]or keys[pygame.K_a]:
        moveLeft()
        if x>-8:    
            x-=3  
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            Light()
            unLight()
            screen.blit(scary,(scaryX,scaryY))    
        
        pygame.display.update()
        lastKey='left'
    if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
        moveRight()
        if x<575:    
            x+=3
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            Light()
            unLight()
            screen.blit(scary,(scaryX,scaryY))
        pygame.display.update()
        lastKey='right'
    if keys[pygame.K_DOWN]or keys[pygame.K_s]:
        if y<570:
            y+=3
        if lastKey=='right':
            moveRight()
        if lastKey=='left':
            moveLeft()
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        
        screen.blit(nightShader,(0,0))
        if darkness>=210:
                Light()
                unLight()
                screen.blit(scary,(scaryX,scaryY))
        pygame.display.update()
        if y>=570 and level==level0:
            level=level1
            x,y=250,0
            screen.blit(nightShader,(0,0))
            darkness+=10
            nightShader.set_alpha(darkness)
            pygame.display.update()
    if keys[pygame.K_UP]or keys[pygame.K_w]:
        if y>3:    
            y-=3
        elif y==0:
            y=1
        if lastKey=='right':
            moveRight()
        if lastKey=='left':
            moveLeft()
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        
        screen.blit(nightShader,(0,0))
        if darkness>=210:
                screen.blit(scary,(scaryX,scaryY))
                Light()
                unLight()
        pygame.display.update()
        if level==level1 and y<=5:
            level=level0
            darkness+=10
            nightShader.set_alpha(darkness)
            
            screen.blit(level,(0,0))
            screen.blit(curentSprite,(x,y))
            screen.blit(nightShader,(0,0))
            if darkness>=210:
                screen.blit(scary,(scaryX,scaryY))
                Light()
            x,y=300,600
            pygame.display.update()    
    print(x,y)
    if keys[pygame.K_LEFT]or keys[pygame.K_a]or keys[pygame.K_RIGHT]or keys[pygame.K_d]or keys[pygame.K_DOWN]or keys[pygame.K_s]or keys[pygame.K_UP]or keys[pygame.K_w]:
        pass
    else:    
        if lastKey=='left':
            curentSprite=dIdL
            screen.blit(level,(0,0))
            screen.blit(curentSprite,(x,y))
            screen.blit(nightShader,(0,0))
            if darkness>=210:
                screen.blit(scary,(scaryX,scaryY))
                nightShader.set_at((x,y),(0,0,0,0))
            pygame.display.update()
        else:
            curentSprite=dId
            screen.blit(level,(0,0))
            screen.blit(curentSprite,(x,y))
            screen.blit(nightShader,(0,0))
            unLight()
            screen.blit(scary,(scaryX,scaryY))
            pygame.display.update()