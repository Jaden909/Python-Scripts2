import pygame
x,y=0,0
screen=pygame.display.set_mode((600,600))
spriteR=pygame.image.load('SpriteR0.png').convert()
spriteU=pygame.image.load('SpriteU0.png').convert()
spriteD=pygame.image.load('SpriteD0.png').convert()
spriteL=pygame.image.load('SpriteL0.png').convert()
Background=pygame.image.load('Background.png').convert()
curentSprite=spriteR
logo=pygame.image.load('LOGOUP.png').convert()

while True:
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
            x-=1
    if keys[pygame.K_RIGHT]:
            x+=1
    if keys[pygame.K_UP]:
            y-=1
    if keys[pygame.K_DOWN]:
            y+=1  
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit()
        
        if event.type==pygame.KEYDOWN:
            
              
            if event.key==pygame.K_RIGHT:
                curentSprite=spriteR
                x+=10
                screen.blit(Background,(0,0))
                screen.blit(curentSprite,(x,y))
            if event.key==pygame.K_LEFT:
                curentSprite=spriteL
                x-=10
                screen.blit(Background,(0,0))
                screen.blit(curentSprite,(x,y))
            if event.key==pygame.K_DOWN:
                curentSprite=spriteD
                y+=10
                screen.blit(Background,(0,0))
                screen.blit(curentSprite,(x,y))
            if event.key==pygame.K_UP:
                curentSprite=spriteU
                y-=10
                screen.blit(Background,(0,0))
                screen.blit(curentSprite,(x,y))
    pygame.display.update()
    pygame.time.wait(100)
