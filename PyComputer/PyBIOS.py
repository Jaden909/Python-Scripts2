import Computer,pygame
font=pygame.font.SysFont('Consolas',16)
titleFont=pygame.font.SysFont('Consolas',24)
bootTitle=titleFont.render('Boot Menu',False,'white')
bootOption1=font.render('Boot Normally',False,'white')
bootOption2=font.render('Boot in Safe Mode (no mods)',False,'white')
bootOption3=font.render('Test Single Mod',False,'white')
bootOption4=font.render('Custom Boot Mods',False,'white')#Would likely break current mods if implemented
selection=font.render('>',False,'white')
selectionNum,selectionMin,selectionMax=200,200,300
mods=True
while True:
    if pygame.event.get(pygame.QUIT):
        exit()
    Computer.screen.fill((0,0,0))
    Computer.screen.blit(bootTitle,(440,100))  
    Computer.screen.blit(bootOption1,(440,200))
    Computer.screen.blit(bootOption2,(440,250))
    Computer.screen.blit(bootOption3,(440,300))
    Computer.screen.blit(selection,(400,selectionNum))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                if selectionNum<selectionMax:
                    selectionNum+=50
            if keys[pygame.K_UP]:
                if selectionNum>selectionMin:
                    selectionNum-=50
            if keys[pygame.K_RETURN]:
                if selectionNum==200:
                    mods=True
                    Computer.booting=True
                    break
                if selectionNum==250:
                    mods=False
                    Computer.booting=True
                    break
                if selectionNum==300:
                    print('not implemented yet')
                    #modTest()
    if Computer.booting:
        Computer.screen.fill((0,0,0))
        Computer.screen.blit(Computer.loadingScreen,(0,0))
        pygame.display.update()
        print('help me')
        break
    pygame.display.update()