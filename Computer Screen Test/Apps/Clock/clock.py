import Computer,pygame,json
meta:dict=json.load(open('Apps\\Clock\\meta.json'))
clockNum0=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum00.png')
clockNum1=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum01.png')
clockNum2=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum02.png')
clockNum3=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum03.png')
clockNum4=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum04.png')
clockNum5=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum05.png')
clockNum6=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum06.png')
clockNum7=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum07.png')
clockNum8=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum08.png')
clockNum9=pygame.image.load('Apps\\Clock\\Media\\clockNums\\clockNum09.png')

def loop():
    Computer.screen.blit(clockNum0,(300,200))
    Computer.screen.blit(clockNum1,(330,200))
    Computer.screen.blit(clockNum2,(360,200))
    Computer.screen.blit(clockNum3,(390,200))
    Computer.screen.blit(clockNum4,(420,200))
    Computer.screen.blit(clockNum5,(450,200))
    Computer.screen.blit(clockNum6,(480,200))
    Computer.screen.blit(clockNum7,(510,200))
    Computer.screen.blit(clockNum8,(540,200))
    Computer.screen.blit(clockNum9,(570,200)) 