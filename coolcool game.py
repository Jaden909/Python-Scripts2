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
dId=pygame.image.load('Dude\\dudeidle.png').convert()
dR=pygame.image.load('Dude\\dudewalking.png').convert()
dR1=pygame.image.load('Dude\\dudewalking1.png').convert()
dL=pygame.image.load('Dude\\dudewalkingleft.png').convert()
dL1=pygame.image.load('Dude\\dudewalkingleft1.png').convert()
dIdL=pygame.image.load('Dude\\dudeidleleft.png').convert()
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
lastKey='right'
Rvalue=0
Lvalue=0
darkness=0
clock=pygame.time.Clock()
level=level0
scaryX=random.choice(range(50,550))
scaryY=random.choice(range(50,550))
ry=0
def changeLevel(changeFrom,changeTo):
    global darkness,x,y,level
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
        level=level8
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
        level=level8
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
        level=level8
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
        #text=font.render(f'Brightness: {brightness}%',True,'white')
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
            #text=font.render(f'Brightness: {brightness}%',True,'white')
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
font=pygame.font.Font('freesansbold.ttf',20)
text=font.render('Brightness:',True,'white')    
screen.blit(text,(50,100))      
pygame.display.update()        
       
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
        darkStuff()
        lastKey='left'
        if x<=10:  
            if level==level7:  
               changeLevel(7,0)
            if level==level8:  
               changeLevel(8,1)  
            if level==level3:  
               changeLevel(3,2)    
            if level==level6:  
               changeLevel(6,7)
            if level==level4:  
               changeLevel(4,3) 
            if level==level5:  
               changeLevel(5,8)
    if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
        moveRight()
        if x<575:    
            x+=3
        screen.blit(level,(0,0))
        screen.blit(curentSprite,(x,y))
        screen.blit(nightShader,(0,0))
        darkStuff()
        lastKey='right'
        if x>=570:  
            if level==level7:  
               changeLevel(7,6)
            if level==level8:  
               changeLevel(8,5)
            if level==level3:  
               changeLevel(3,4)
            if level==level1:  
               changeLevel(1,8)
            if level==level2:  
               changeLevel(2,3) 
            if level==level0:  
               changeLevel(0,7)
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
        darkStuff()
        if y>=570:  
            if level==level1:  
               changeLevel(1,2)
            if level==level8:  
               changeLevel(8,3)
            if level==level5:  
               changeLevel(5,4)   
            if level==level0:  
               changeLevel(0,1) 
            if level==level7:  
               changeLevel(7,8)
            if level==level6:  
               changeLevel(6,5)
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
        darkStuff()
        if y<5:   
            if level==level1:  
               changeLevel(1,0)
            if level==level8:  
               changeLevel(8,7)
            if level==level5:  
               changeLevel(5,6)
            if level==level2:  
               changeLevel(2,1) 
            if level==level3:  
               changeLevel(3,8)
            if level==level4:  
               changeLevel(4,5)
    print(x,y)
    if keys[pygame.K_LEFT]or keys[pygame.K_a]or keys[pygame.K_RIGHT]or keys[pygame.K_d]or keys[pygame.K_DOWN]or keys[pygame.K_s]or keys[pygame.K_UP]or keys[pygame.K_w]:
        pass
    else:    
        if lastKey=='left':
            curentSprite=dIdL
            screen.blit(level,(0,0))
            screen.blit(curentSprite,(x,y))
            screen.blit(nightShader,(0,0))
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
            unLight()
            if darkness>=210:
                screen.blit(scary,(scaryX,scaryY))
                screen.blit(text,(20,20))
                if brightness<=20:
                   moveScary()
            pygame.display.update()