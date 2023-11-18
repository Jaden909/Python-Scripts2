import Computer,pygame,time,customtkinter,PyEngine
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
configVars=PyEngine.load('Apps\\Clock\\config.json')
use24hrtime=configVars.get('use24hrtime')

def loop():
    #print(time.localtime())
    curTime=time.localtime()
    if not use24hrtime:
        if curTime.tm_hour==1 or curTime.tm_hour==13:
            Computer.screen.blit(clockNum1,(1040,624))
        if curTime.tm_hour==2 or curTime.tm_hour==14:
            Computer.screen.blit(clockNum2,(1040,624))
        if curTime.tm_hour==3 or curTime.tm_hour==15:
            Computer.screen.blit(clockNum3,(1040,624))
        if curTime.tm_hour==4 or curTime.tm_hour==16:
            Computer.screen.blit(clockNum4,(1040,624))
        if curTime.tm_hour==5 or curTime.tm_hour==17:
            Computer.screen.blit(clockNum5,(1040,624))
        if curTime.tm_hour==6 or curTime.tm_hour==18:
            Computer.screen.blit(clockNum6,(1040,624))
        if curTime.tm_hour==7 or curTime.tm_hour==19:
            Computer.screen.blit(clockNum7,(1040,624))
        if curTime.tm_hour==8 or curTime.tm_hour==20:
            Computer.screen.blit(clockNum8,(1040,624))
        if curTime.tm_hour==9 or curTime.tm_hour==21:
            Computer.screen.blit(clockNum9,(1040,624))
        if curTime.tm_hour==10 or curTime.tm_hour==22:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum0,(1040,624))
        if curTime.tm_hour==11 or curTime.tm_hour==23:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum1,(1040,624))
        if curTime.tm_hour==12 or curTime.tm_hour==0:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum2,(1040,624))
    if use24hrtime:
        if curTime.tm_hour==1:
            Computer.screen.blit(clockNum1,(1040,624))
        if curTime.tm_hour==2:
            Computer.screen.blit(clockNum2,(1040,624))
        if curTime.tm_hour==3:
            Computer.screen.blit(clockNum3,(1040,624))
        if curTime.tm_hour==4:
            Computer.screen.blit(clockNum4,(1040,624))
        if curTime.tm_hour==5:
            Computer.screen.blit(clockNum5,(1040,624))
        if curTime.tm_hour==6:
            Computer.screen.blit(clockNum6,(1040,624))
        if curTime.tm_hour==7:
            Computer.screen.blit(clockNum7,(1040,624))
        if curTime.tm_hour==8:
            Computer.screen.blit(clockNum8,(1040,624))
        if curTime.tm_hour==9:
            Computer.screen.blit(clockNum9,(1040,624))
        if curTime.tm_hour==10:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum0,(1040,624))
        if curTime.tm_hour==11:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum1,(1040,624))
        if curTime.tm_hour==12:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum2,(1040,624))
        if curTime.tm_hour==13:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum3,(1040,624))
        if curTime.tm_hour==14:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum4,(1040,624))
        if curTime.tm_hour==15:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum5,(1040,624))
        if curTime.tm_hour==16:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum6,(1040,624))
        if curTime.tm_hour==17:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum7,(1040,624))
        if curTime.tm_hour==18:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum8,(1040,624))
        if curTime.tm_hour==19:
            Computer.screen.blit(clockNum1,(976,624))
            Computer.screen.blit(clockNum9,(1040,624))
        if curTime.tm_hour==20:
            Computer.screen.blit(clockNum2,(976,624))
            Computer.screen.blit(clockNum0,(1040,624))
        if curTime.tm_hour==21:
            Computer.screen.blit(clockNum2,(976,624))
            Computer.screen.blit(clockNum1,(1040,624))
        if curTime.tm_hour==22:
            Computer.screen.blit(clockNum2,(976,624))
            Computer.screen.blit(clockNum2,(1040,624))
        if curTime.tm_hour==23:
            Computer.screen.blit(clockNum2,(976,624))
            Computer.screen.blit(clockNum3,(1040,624))
        if curTime.tm_hour==0:
            Computer.screen.blit(clockNum0,(976,624))
            Computer.screen.blit(clockNum0,(1040,624))
    if len(str(curTime.tm_min))==2:
        if str(curTime.tm_min)[0]=='1':
            Computer.screen.blit(clockNum1,(1136,624))
        if str(curTime.tm_min)[0]=='2':
            Computer.screen.blit(clockNum2,(1136,624))
        if str(curTime.tm_min)[0]=='3':
            Computer.screen.blit(clockNum3,(1136,624))
        if str(curTime.tm_min)[0]=='4':
            Computer.screen.blit(clockNum4,(1136,624))
        if str(curTime.tm_min)[0]=='5':
            Computer.screen.blit(clockNum5,(1136,624))
        if str(curTime.tm_min)[1]=='0':
            Computer.screen.blit(clockNum0,(1200,624))
        if str(curTime.tm_min)[1]=='1':
            Computer.screen.blit(clockNum1,(1200,624))
        if str(curTime.tm_min)[1]=='2':
            Computer.screen.blit(clockNum2,(1200,624))
        if str(curTime.tm_min)[1]=='3':
            Computer.screen.blit(clockNum3,(1200,624))
        if str(curTime.tm_min)[1]=='4':
            Computer.screen.blit(clockNum4,(1200,624))
        if str(curTime.tm_min)[1]=='5':
            Computer.screen.blit(clockNum5,(1200,624))
        if str(curTime.tm_min)[1]=='6':
            Computer.screen.blit(clockNum6,(1200,624))
        if str(curTime.tm_min)[1]=='7':
            Computer.screen.blit(clockNum7,(1200,624))
        if str(curTime.tm_min)[1]=='8':
            Computer.screen.blit(clockNum8,(1200,624))
        if str(curTime.tm_min)[1]=='9':
            Computer.screen.blit(clockNum9,(1200,624))
    if len(str(curTime.tm_min))==1:
        if curTime.tm_min==0:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum0,(1200,624))
        if curTime.tm_min==1:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum1,(1200,624))
        if curTime.tm_min==2:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum2,(1200,624))
        if curTime.tm_min==3:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum3,(1200,624))
        if curTime.tm_min==4:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum4,(1200,624))
        if curTime.tm_min==5:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum5,(1200,624))
        if curTime.tm_min==6:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum6,(1200,624))
        if curTime.tm_min==7:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum7,(1200,624))
        if curTime.tm_min==8:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum8,(1200,624))
        if curTime.tm_min==9:
            Computer.screen.blit(clockNum0,(1136,624))
            Computer.screen.blit(clockNum9,(1200,624)) 
    #Position 1 (976,624)
    #Position 2 (1040,624)
    #Position 3 (1136,624)
    #Position 4 (1200,624)
def config():
    global configVars
    def setTrue():
        global use24hrtime
        use24hrtime=True
    def setFalse():
        global use24hrtime
        use24hrtime=False
    mainWin=customtkinter.CTk()
    mainWin.geometry('200x100')
    mainWin.title('Clock Config')
    label24hr=customtkinter.CTkLabel(text='Use 24-Hour Time?',width=20)
    trueButt=customtkinter.CTkButton(text='Yes',width=20,command=setTrue)
    falseButt=customtkinter.CTkButton(text='No',width=20,command=setFalse)
    label24hr.place(x=50,y=1)
    trueButt.place(x=60,y=30)
    falseButt.place(x=115,y=30)
    mainWin.mainloop()
    configVars.update(use24hrtime=use24hrtime)
    PyEngine.save('Apps\\Clock\\config.json',configVars)
#config()