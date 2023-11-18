import pygame
import random
pygame.init()
x,y=0,0
screen=pygame.display.set_mode((600,600))
level0Night=pygame.image.load('level0Night.png').convert()
level0=pygame.image.load('level0.png').convert()
level1=pygame.image.load('level1.png').convert()
level2=pygame.image.load('level2.png').convert()
level3=pygame.image.load('level3.png').convert()
level4=pygame.image.load('level4.png').convert()
level5=pygame.image.load('level5.png').convert()
level6=pygame.image.load('level6.png').convert()
level7=pygame.image.load('level7.png').convert()
level8=pygame.image.load('level8.png').convert()
level8a=pygame.image.load('level8a.png').convert()
dId=pygame.image.load('Dude\\dudeidle.png').convert()
dR=pygame.image.load('Dude\\dudewalking.png').convert()
dR1=pygame.image.load('Dude\\dudewalking1.png').convert()
dL=pygame.image.load('Dude\\dudewalkingleft.png').convert()
dL1=pygame.image.load('Dude\\dudewalkingleft1.png').convert()
dIdL=pygame.image.load('Dude\\dudeidleleft.png').convert()
nightShader=pygame.image.load('night.png').convert_alpha()
scary=pygame.image.load('scary.png').convert()
title=pygame.image.load('Title.png').convert()
nightShader.set_alpha(0)
scary.set_colorkey((0,0,0))
dId.set_colorkey((0,0,0))
dR.set_colorkey((0,0,0))
dR1.set_colorkey((0,0,0))
dL.set_colorkey((0,0,0))
dL1.set_colorkey((0,0,0))
dIdL.set_colorkey((0,0,0))
lastKey='right'
Rvalue=0
Lvalue=0
darkness=0
visited8=0
started=0
font=pygame.font.SysFont('comicsansms',30)
font2=pygame.font.SysFont('comicsansms',70)
font3=pygame.font.SysFont('comicsansms',10)
Keys=0
#end game: random fill pixels white and then fill and then victory screen
#Lines
text=font.render('You found a key!',True,'white')
textStart=font.render('Looks like I need to find some Keys...',True,'white')
textEnd=font.render('Maybe I should toss a coin in...',True,'white')
text1=font.render('You found a coin!',True,'white')  
textKeys=font.render('Keys collected:',True,'white')
textKeysValue=font.render(f'{Keys}/4',True,'white')
textComplete=font.render('The Doors should be unlocked now...',True,'white')
textOver=font2.render('You Win!',True,'black')
textVer=font3.render('A Walk in the Park v0.1 DEVELOPMENT BUILD',True,'white')

gameOver=0
titleScreen=0
clock=pygame.time.Clock()
level=level0
scaryX=random.choice(range(50,550))
scaryY=random.choice(range(50,550))
ry=0
#DEBUG ONLY
unlock=0
found1,found2,found3,found4,found5,foundc=0,0,0,0,0,0
doorsUnlocked=0
def changeLevel(changeFrom,changeTo):
    global darkness,x,y,level,visited8,doorsUnlocked
    #Level0--->Level1
    if changeTo==1 and changeFrom==0:    
        level=level1
        x,y=250,0
        screen.blit(nightShader,(0,0))
        nightShader.fill('black')
        darkness+=10
        nightShader.set_alpha(darkness)
        pygame.display.update()
        return
    #Level1--->Level0
    if changeTo==0 and changeFrom==1:
        level=level0
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,600
        pygame.display.update() 
        return
    #Level1--->Level2
    if changeFrom==1 and changeTo==2:
        level=level2
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,0
        pygame.display.update() 
        return  
    #Level1--->level8
    if changeFrom==1 and changeTo==8:
        if doorsUnlocked==1:
            level=level8a
        else:
            level=level8
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=30,300
        pygame.display.update() 
        if visited8==0:
            screen.blit(textStart,(50,550))
            screen.blit(textKeys,(50,50))
            screen.blit(textKeysValue,(100,50))
            visited8=1
            pygame.display.update()
            pygame.time.wait(2000)
            return
        return 
    #Level2--->Level1
    if changeFrom==2 and changeTo==1:
        level=level1
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,600
        pygame.display.update() 
        return 
    # Level2--->level3
    if changeFrom==2 and changeTo==3:
        level=level3
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=30,300
        pygame.display.update() 
        return 
    # level3-->level4
    if changeFrom==3 and changeTo==4:
        level=level4
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=30,300
        pygame.display.update() 
        return 
    # level3---> level2
    if changeFrom==3 and changeTo==2:
        level=level2
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=580,300
        pygame.display.update() 
        return 
    #level3--->level8
    if changeFrom==3 and changeTo==8:
        if doorsUnlocked==1:
            level=level8a
        else:level=level8
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,600
        if visited8==0:
            screen.blit(textStart,(50,50))
            screen.blit(textKeys,(50,50))
            screen.blit(textKeysValue,(100,50))
            visited8=1
            pygame.display.update()
            pygame.time.wait(2000)
            return
        pygame.display.update() 
        return 
    #Level4--->level3
    if changeFrom==4 and changeTo==3:
        level=level3
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=580,300
        pygame.display.update() 
        return 
    #level4--->5
    if changeFrom==4 and changeTo==5:
        level=level5
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,600
        pygame.display.update() 
        return 
    #5-->8
    if changeFrom==5 and changeTo==8:
        if doorsUnlocked==1:
            level=level8a
        else:level=level8
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=580,300
        if visited8==0:
            screen.blit(textStart,(50,50))
            screen.blit(textKeys,(50,50))
            screen.blit(textKeysValue,(100,50))
            visited8=1
            pygame.display.update()
            pygame.time.wait(2000)
            return
        pygame.display.update() 
        return 
    #5-->6
    if changeFrom==5 and changeTo==6:
        level=level6
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,600
        pygame.display.update() 
        return 
    #5-->4
    if changeFrom==5 and changeTo==4:
        level=level4
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,0
        pygame.display.update() 
        return 
    #6-->7
    if changeFrom==6 and changeTo==7:
        level=level7
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=580,300
        pygame.display.update() 
        return 
    #6-5
    if changeFrom==6 and changeTo==5:
        level=level5
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,0
        pygame.display.update() 
        return 
    #7-0
    if changeFrom==7 and changeTo==0:
        level=level0
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=580,300
        pygame.display.update() 
        return 
    #7-6
    if changeFrom==7 and changeTo==6:
        level=level6
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=30,300
        pygame.display.update() 
        return 
    #7-8
    if changeFrom==7 and changeTo==8:
        if doorsUnlocked==1:
            level=level8a
        else:level=level8
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,0
        if visited8==0:
            screen.blit(textStart,(50,50))
            screen.blit(textKeys,(50,50))
            screen.blit(textKeysValue,(100,50))
            visited8=1
            pygame.display.update()
            pygame.time.wait(2000)
            return
        pygame.display.update() 
        return 
    #0-7
    if changeFrom==0 and changeTo==7:
        level=level7
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=30,300
        pygame.display.update() 
        return 
    #8-1
    if changeFrom==8 and changeTo==1:
        level=level1
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=580,300
        pygame.display.update() 
        return 
    #8-7
    if changeFrom==8 and changeTo==7:
        level=level7
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,600
        pygame.display.update() 
        return 
    #8-5
    if changeFrom==8 and changeTo==5:
        level=level5
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=30,300
        pygame.display.update() 
        return 
    #8-3
    if changeFrom==8 and changeTo==3:
        level=level3
        darkness+=10
        nightShader.set_alpha(darkness)
        nightShader.fill('black')
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        if darkness>=210:
            screen.blit(scary,(scaryX,scaryY))
        x,y=300,0
        pygame.display.update() 
        return 
def darkStuff():    
    global darkness
    if darkness>=210:
        Light()
        unLight()
        screen.blit(scary,(scaryX,scaryY))    
        screen.blit(text,(20,20))
        pygame.display.update()
def moveRight():
    moveList=[dR,dR,dR,dR,dR,dR1,dR1,dR1,dR1,dR1]
    global Rvalue,curentSprite,clock
    clock.tick(60)
    curentSprite=moveList[Rvalue]
    Rvalue+=1
    if Rvalue>=len(moveList):
        Rvalue=0
    pygame.display.update()
def moveLeft():
    moveList=[dL,dL,dL,dL,dL,dL1,dL1,dL1,dL1,dL1]
    global Lvalue,curentSprite,clock
    clock.tick(60)
    curentSprite=moveList[Lvalue]
    Lvalue+=1
    if Lvalue>=len(moveList):
        Lvalue=0
    pygame.display.update()
def interact():
    global level,x,y,found1,Keys,found2,found3,found4,doorsUnlocked,found5,foundc,gameOver
    if level==level1 and x>200 and x<300 and y>200 and y<300 and found1==0:
        print('you found a key!')
        found1=1
        Keys+=1
        screen.blit(text,(50,500))      
        pygame.display.update() 
        pygame.time.wait(1000)
        if Keys==4:
            screen.blit(textComplete,(0,600))
            pygame.display.update()
            pygame.time.wait(2000)
            doorsUnlocked=1
        return
    if level==level7 and x>250 and x<300 and y>250 and y<300 and found2==0:
        print('you found a key!')
        found2=1
        Keys+=1
        screen.blit(text,(50,500))      
        pygame.display.update() 
        pygame.time.wait(1000)
        if Keys==4:
            screen.blit(textComplete,(0,600))
            pygame.display.update()
            pygame.time.wait(2000)
            doorsUnlocked=1
        return
    if level==level3 and x>300 and x<350 and y>500 and y<550 and found3==0:
        print('you found a key!')
        found3=1
        Keys+=1
        screen.blit(text,(50,500))      
        pygame.display.update() 
        pygame.time.wait(1000)
        if Keys==4:
            screen.blit(textComplete,(0,600))
            pygame.display.update()
            pygame.time.wait(2000)
            doorsUnlocked=1
        return
    if level==level6 and x>450 and y<30 and found4==0:
        print('you found a key!')
        found4=1
        Keys+=1
        screen.blit(text,(50,500))      
        pygame.display.update() 
        pygame.time.wait(1000)
        if Keys==4:
            screen.blit(textComplete,(0,600))
            pygame.display.update()
            pygame.time.wait(2000)
            doorsUnlocked=1
        return
    if level==level8a and x>250 and x<300 and y>300 and y<350 and found5==0:
        found5=1
        screen.blit(textEnd,(50,500))      
        pygame.display.update() 
        pygame.time.wait(1000)
        return
    if level==level2 and x>50 and x<100 and y>450 and y<500 and foundc==0:
        foundc=1
        screen.blit(text1,(50,500))
        pygame.display.update() 
        pygame.time.wait(1000)
        return
    if level==level8a and x>250 and x<300 and y>300 and y<350 and foundc==1:
        for jj in range(10000):   
            nx=list(range(601))
            ny=list(range(601))
            nightShader.set_at((random.choice(nx),random.choice(ny)),(255,255,255,255))      
            pygame.display.update() 
        nightShader.fill((255,255,255))
        nightShader.set_alpha(255)
        screen.blit(textOver,(150,150))
        gameOver=1
        return
curentSprite=dId
logo=pygame.image.load('LOGOUP.png').convert()
screen.blit(curentSprite,(x,y))
lightRange=30
litPixels=0
def Light():
    nx=list(range(lightRange))
    ny=list(range(lightRange))
    global litPixels,text,brightness
    if darkness>=210:
        for i in range(lightRange):
            itemx=random.choice(range(len(nx)))
            itemy=random.choice(range(len(ny)))
            _=nightShader.get_at((itemx,itemy))
            if _==(0,0,0,255):
                nightShader.set_at((x-nx[itemx],y-ny[itemy]),(0,0,0,0))
                litPixels+=1
            nx.pop(itemx)
            ny.pop(itemy)
        nx=list(range(lightRange))
        ny=list(range(lightRange))
        for i in range (lightRange):
            itemx=random.choice(range(len(nx)))
            itemy=random.choice(range(len(ny)))
            _=nightShader.get_at((itemx,itemy))
            if _==(0,0,0,255):
                nightShader.set_at((x+nx[itemx],y+ny[itemy]),(0,0,0,0))
                litPixels+=1
            nx.pop(itemx)
            ny.pop(itemy) 
        nx=list(range(lightRange))
        ny=list(range(lightRange))
        for i in range (lightRange):
            itemx=random.choice(range(len(nx)))
            itemy=random.choice(range(len(ny)))
            _=nightShader.get_at((itemx,itemy))
            if _==(0,0,0,255):
                nightShader.set_at((x-nx[itemx],y+ny[itemy]),(0,0,0,0))
                litPixels+=1
            nx.pop(itemx)
            ny.pop(itemy)  
        nx=list(range(lightRange))
        ny=list(range(lightRange))
        for i in range (lightRange):
            itemx=random.choice(range(len(nx)))
            itemy=random.choice(range(len(ny)))
            _=nightShader.get_at((itemx,itemy))
            if _==(0,0,0,255):
                nightShader.set_at((x+nx[itemx],y-ny[itemy]),(0,0,0,0))
                litPixels+=1
            nx.pop(itemx)
            ny.pop(itemy)
        brightness=litPixels/3600
def unLight():
    global litPixels,text,brightness
    if darkness>=210:
        for i in range(600):
            item=(random.choice(range(600)),random.choice(range(600)))
            _=nightShader.get_at(item)
            if  _!=(0,0,0,255):  
                nightShader.set_at(item,(0,0,0,255))
                if litPixels!=0: 
                    litPixels-=1
            brightness=litPixels/3600
def moveScary():
    global scaryX,scaryY,x,y
    if x>scaryX:
        scaryX+=1
    else: scaryX-=1 
    if y>scaryY:
        scaryY+=1
    else: scaryY-=1
    screen.blit(scary,(scaryX,scaryY))
    pygame.display.update()
    if scaryX==x and scaryY==y:
        deathCheck=nightShader.get_at((random.choice(range(600)),random.choice(range(600))))
        if deathCheck==(110,0,0,255):
            print('You Died!')
            exit()
        nightShader.fill((255,0,0,255))
        screen.blit(nightShader,(0,0))
        pygame.display.update()
        pygame.time.wait(100)
        nightShader.fill((225,0,0,255))
        screen.blit(nightShader,(0,0))
        pygame.display.update()
        pygame.time.wait(100) 
        nightShader.fill((200,0,0,255))
        screen.blit(nightShader,(0,0))
        pygame.display.update()
        pygame.time.wait(100) 
        nightShader.fill((170,0,0,255))
        screen.blit(nightShader,(0,0))
        pygame.display.update()
        pygame.time.wait(100) 
        nightShader.fill((140,0,0,255))
        screen.blit(nightShader,(0,0))
        pygame.display.update()
        pygame.time.wait(100)  
        nightShader.fill((110,0,0,255))
        screen.blit(nightShader,(0,0))
        pygame.display.update()
        pygame.time.wait(1000)
    pygame.time.wait(50)          

while True:    
    if titleScreen==0:   
        screen.blit(title,(0,0))
        screen.blit(textVer,(0,585))
        pygame.display.update()
        titleScreen=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    left,middle,right=pygame.mouse.get_pressed()
    if left:
        mouseX,mouseY=pygame.mouse.get_pos()
        print(mouseX,mouseY)
        if mouseX>165 and mouseX<460 and mouseY>402 and mouseY<488:
            started=1
            break
if started==1:   
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
            screen.blit(textVer,(0,585))
            if visited8==1:
                screen.blit(textKeys,(0,0))
                screen.blit(textKeysValue,(220,0))
            darkStuff()
            lastKey='left'
            if x<=10:  
                if level==level7:  
                   changeLevel(7,0)
                if level==level8 or level==level8a:  
                   changeLevel(8,1)  
                if level==level3:  
                   changeLevel(3,2)    
                if level==level6:  
                   changeLevel(6,7)
                if level==level4:  
                   changeLevel(4,3) 
                if level==level5:  
                   changeLevel(5,8)
            if x>200 and x<370 and y>200 and y<400 and level==level8 and unlock==0 or x>200 and x<370 and y>200 and y<400 and level==level8a and unlock==0:
                x,y=450,300
        if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            moveRight()
            if x<575:    
                x+=3
            screen.blit(level,(0,0))
            screen.blit(curentSprite,(x,y))
            screen.blit(nightShader,(0,0))
            screen.blit(textVer,(0,585))
            if visited8==1:
                screen.blit(textKeys,(0,0))
                screen.blit(textKeysValue,(220,0))
            darkStuff()
            lastKey='right'
            if x>=570:  
                if level==level7:  
                   changeLevel(7,6)
                if level==level8 or level==level8a:  
                   changeLevel(8,5)
                if level==level3:  
                   changeLevel(3,4)
                if level==level1:  
                   changeLevel(1,8)
                if level==level2:  
                   changeLevel(2,3) 
                if level==level0:  
                   changeLevel(0,7)
            if x>200 and x<370 and y>200 and y<400 and level==level8 and unlock==0 or x>200 and x<370 and y>200 and y<400 and level==level8a and unlock==0:
                x,y=150,300
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
            screen.blit(textVer,(0,585))
            if visited8==1:
                screen.blit(textKeys,(0,0))
                screen.blit(textKeysValue,(220,0))
            darkStuff()
            if y>=570:  
                if level==level1:  
                   changeLevel(1,2)
                if level==level8 or level==level8a:  
                   changeLevel(8,3)
                if level==level5:  
                   changeLevel(5,4)   
                if level==level0:  
                   changeLevel(0,1) 
                if level==level7:  
                   changeLevel(7,8)
                if level==level6:  
                   changeLevel(6,5)
            if x>200 and x<370 and y>200 and y<400 and level==level8 and unlock==0 and doorsUnlocked==1:
                x,y=300,150
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
            screen.blit(textVer,(0,585))
            if visited8==1:
                screen.blit(textKeys,(0,0))
                screen.blit(textKeysValue,(220,0))
            darkStuff()
            if y<5:   
                if level==level1:  
                   changeLevel(1,0)
                if level==level8 or level==level8a:  
                   changeLevel(8,7)
                if level==level5:  
                   changeLevel(5,6)
                if level==level2:  
                   changeLevel(2,1) 
                if level==level3:  
                   changeLevel(3,8)
                if level==level4:  
                   changeLevel(4,5)
            if x>200 and x<370 and y>200 and y<400 and level==level8 and unlock==0 or x>200 and x<370 and y>200 and y<400 and level==level8a and unlock==0:
                x,y=300,450
        #print(x,y)
        left,middle,right=pygame.mouse.get_pressed()
        if left:
            interact()
            textKeysValue=font.render(f'{Keys}/4',True,'white')
        if visited8==1:
            screen.blit(textKeys,(0,0))
            screen.blit(textKeysValue,(220,0))
        if keys[pygame.K_LEFT]or keys[pygame.K_a]or keys[pygame.K_RIGHT]or keys[pygame.K_d]or keys[pygame.K_DOWN]or keys[pygame.K_s]or keys[pygame.K_UP]or keys[pygame.K_w]:
            pass
        else:    
            if lastKey=='left':
                curentSprite=dIdL
                screen.blit(level,(0,0))
                screen.blit(curentSprite,(x,y))
                screen.blit(nightShader,(0,0))
                screen.blit(textVer,(0,585))
                if visited8==1:
                    screen.blit(textKeys,(0,0))
                    screen.blit(textKeysValue,(220,0))
                unLight()
                if darkness>=210:
                    screen.blit(scary,(scaryX,scaryY))
                    screen.blit(text,(20,20))
                    if brightness<=20:
                       moveScary() 
                pygame.display.update()
            else:
                curentSprite=dId
                screen.blit(level,(0,0))
                screen.blit(curentSprite,(x,y))
                screen.blit(nightShader,(0,0))
                screen.blit(textVer,(0,585))
                if visited8==1:
                    screen.blit(textKeys,(0,0))
                    screen.blit(textKeysValue,(220,0))
                unLight()
                if darkness>=210:
                    screen.blit(scary,(scaryX,scaryY))
                    screen.blit(text,(20,20))
                    if brightness<=20:
                       moveScary()
                pygame.display.update()
            if gameOver==1:
                screen.blit(nightShader,(0,0))
                screen.blit(textOver,(150,150))
                pygame.display.update()
                pygame.time.wait(10000)
                exit()
