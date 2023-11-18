debugMode=0
from tkinter import *
from tkinter.ttk import Progressbar
hpDisplay=550
manaDisplay=550
xpDisplay=50
gameStarted=0
event='none'
dmgTaken=0
#Player Base Stats
class player:
    hp=50
    mana=100
    xp=0
    level=1
    maxHp=100
    maxMana=100
    attack=2
    defense=1
    luck=1
    critChance=1
    coins=0
    BaseAtk=1
    BaseDef=1
    BaseLuk=1
    BaseCrt=1
#Title Screen
mainWin=Tk()
Tk.title(mainWin,'ConRPG')
def startGame():
    global mainWin,gameStarted
    mainWin.destroy()
    gameStarted=1
def debug():
    global debugMode
    debugMode=1
mainWin.geometry('600x600')
pic=PhotoImage(file='Python\\ConRPG\\Assets\\Logo\\LOGOMED.png',master=mainWin)
label=Label(mainWin)
label['image']=pic
title=Label(mainWin,text='ConRPG')
title.config(font=(50))
startB=Button(mainWin, text='Start',command=startGame,height=3,width=25)
startB.config(font=(50))
debugToggle=Checkbutton(mainWin,text='Debug Mode',command=debug)
label.pack()
title.pack()
startB.pack()
debugToggle.pack()
mainWin.mainloop()
#Game code

if gameStarted==1:
    currentWeapon='sword1'
    canWin=Tk()
    Tk.title(canWin,'ConRPG')
    mainCan=Canvas(canWin, width=600,height=600, background='grey75')
    mainCan.pack()
    import ModRPG 
    ModRPG.start(mainCan)
    #HP Bar
    mainCan.create_rectangle(50,500,550,550,fill='grey60')
    mainCan.create_rectangle(50,500,hpDisplay,550,fill='light green',tags='hp')
    #Mana Bar
    mainCan.create_rectangle(50,425,550,475,fill='grey60')
    mainCan.create_rectangle(50,425,manaDisplay,475,fill='sky blue',tags='mana')
    #XP Bar
    mainCan.create_rectangle(50,350,550,400,fill='grey60')
    mainCan.create_rectangle(50,350,xpDisplay,400,fill='#eded68',tags='xp') 

    mainCan.create_oval(50,150,70,170,fill='yellow')
    
    
    sword2Count=0
    sword2State='locked'
    sword3Count=0
    sword3State='locked'
    Turn=0
    UnlockButt=Button(mainCan,text='Unlock All',command=ModRPG.unlockAll,state='disabled')
    give1Butt=Button(mainCan,text='Give 1 all',command=ModRPG.giveAll)
    allUnlocked=False
    #____________________________________________________________Inventory_________________________________________________________________________
    #Inv Window
    def openInv():
        InvWin=Tk()
        Tk.title(InvWin,'Inventory')
        InvWin.geometry('500x500')
        Inv=Canvas(InvWin,width=500,height=500,background='grey75')
        Inv.pack()
        def showLocked(x:float,y:float):    
            lockedImage=PhotoImage(master=Inv,file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\Misc\\unknownItemx64.png')
            lockedLabel=Label(Inv,image=lockedImage)
            lockedLabel.photo=lockedImage
            UnknownTitle=Label(Inv,text='Unknown Item',background='grey75')
            UnknownDesc=Label(Inv,text="Unknown Item. Keep exploring to discover more items",wraplength=150,height=4,width=20,highlightthickness=1,highlightbackground='black')
            Inv.create_window(x,y,window=lockedLabel)
            Inv.create_window(x,y-48,window=UnknownTitle)
            Inv.create_window(x+120,y,window=UnknownDesc)
        def back():
            global UnlockButt
            invButt.config(state='active')
            UnlockButt.config(state='active')
            InvWin.destroy()
        global invButt
        invButt.config(state='disabled')
        backButt=Button(Inv,text='Back',command=back)
        Inv.create_window(250,450,window=backButt)
        #Inv Items
        class sword1:
            state='unlocked'
            #0=no durability loss
            dur=0
            #stat increases
            atk=1
            defense=0
            luck=0
            crt=0
            swordSprite=PhotoImage(master=Inv,file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\Misc\\swordx64.png')
            swordLabel=Label(Inv,image=swordSprite,highlightbackground='black',background='grey50',highlightthickness=1)
            swordLabel.photo=swordSprite
            swordDesc=Label(Inv,text="A basic sword for slaying basic monsters. Doesn't break",wraplength=150,height=4,width=20,highlightthickness=1,highlightbackground='black')
            swordTitle=Label(Inv,text='Basic Sword',background='grey75')
            atkLab=Label(Inv,text=f'+{atk} atk',foreground='red',background='grey75')
            def equip():
                global currentWeapon
                currentWeapon='sword1'
                ModRPG.resetItemStats()
                player.attack=player.attack+sword1.atk
                sword1.equipButt.config(state='disabled',text='Equipped')
                sword2.equipButt.config(state='active',text='Equip')
                atkStr.set(f'Atk: {player.attack}')
            equipButt=Button(Inv,text='Equipped',command=equip,state='disabled')
            def show():
                Inv.create_window(50,60,window=sword1.swordLabel)
                Inv.create_window(170,60,window=sword1.swordDesc)
                Inv.create_window(50,12,window=sword1.swordTitle)
                Inv.create_window(50,110,window=sword1.equipButt)
                Inv.create_window(100,110,window=sword1.atkLab)
        def place(Pos:int,label:Label,desc:Label,Title:Label,equipButt:Button,atkLab:Label,crtLab:Label,countLab:Label):
            if Pos==0:
                Inv.create_window(50,60,window=label)
                Inv.create_window(170,60,window=desc)
                Inv.create_window(50,12,window=Title)
                Inv.create_window(50,110,window=equipButt)
                Inv.create_window(100,110,window=atkLab)
                Inv.create_window(135,110,window=crtLab)
                Inv.create_window(230,110,window=countLab)
            if Pos==1:
                Inv.create_window(300,60,window=label)
                Inv.create_window(420,60,window=desc)
                Inv.create_window(300,12,window=Title)
                Inv.create_window(300,110,window=equipButt)
                Inv.create_window(350,110,window=atkLab)
                Inv.create_window(385,110,window=crtLab)
                Inv.create_window(480,110,window=countLab)
            if Pos==2:
                Inv.create_window(50,200,window=label)
                Inv.create_window(170,200,window=desc)
                Inv.create_window(50,152,window=Title)
                Inv.create_window(50,250,window=equipButt)
                Inv.create_window(100,250,window=atkLab)
                Inv.create_window(135,250,window=crtLab)
                Inv.create_window(230,250,window=countLab)
        def createItem(Type:str,Id:str,Pos:int,Dur:int,MaxDur:int,Atk:int,Defense:int,Luck:int,Crt:int,SpriteFile:str,Desc:str,Title:str):
            class _:
                
                #used to determine position on ui(word for tab, 0 for first, 5 for last)
                id=Id
                #0=no durability loss
                dur=Dur
                maxDur=MaxDur
                #stat increases
                atk=Atk
                defense=Defense
                luck=Luck
                crt=Crt
                sprite=PhotoImage(master=Inv,file=SpriteFile)
                label=Label(Inv,image=sprite,highlightbackground='black',background='grey50',highlightthickness=1)
                label.photo=sprite
                desc=Label(Inv,text=Desc,wraplength=150,height=4,width=20,highlightthickness=1,highlightbackground='black')
                title=Label(Inv,text=Title,background='grey75')
                
                if Type=='sword':    
                    atkLab=Label(Inv,text=f'+{atk} atk',foreground='red',background='grey75')
                    crtLab=Label(Inv,text=f'+{crt} crt',foreground='#FF8E00',background='grey75')
                def equip():
                    if Type=='sword':    
                        global currentWeapon
                        currentWeapon=Id   
                        if Id=='sword2':
                            sword1.equipButt.config(state='active',text='Equip')
                            sword3.equipButt.config(state='active',text='Equip')
                        if Id=='sword3':
                            sword2.equipButt.config(state='active',text='Equip')
                            sword1.equipButt.config(state='active',text='Equip')
                    ModRPG.resetItemStats(player)
                    player.attack,player.critChance=player.attack+_.atk,player.critChance+_.crt
                    _.equipButt.config(state='disabled',text='Equipped')
                    atkStr.set(f'Atk: {player.attack}')
                    crtStr.set(f'Crt: {player.critChance}')
                #State should usually be active
                equipButt=Button(Inv,text='Equip',command=equip,state='active')
                def showInv():
                    if Pos==1:
                        if Id=='sword2':    
                            countLab=Label(Inv,text=f'x{sword2Count}',background='grey75')
                            if sword2State=='unlocked':
                                place(1,_.label,_.desc,_.title,_.equipButt,_.atkLab,_.crtLab,countLab)
                                if sword2Count==0:
                                    _.equipButt.config(state='disabled',text='Out of Item')
                            elif allUnlocked==True:
                                place(1,_.label,_.desc,_.title,_.equipButt,_.atkLab,_.crtLab,countLab)
                                if sword2Count==0:
                                    _.equipButt.config(state='disabled',text='Out of Item')
                            elif sword2State=='locked':
                                showLocked(300,60)
                    if Pos==2:
                        if Id=='sword3':    
                            countLab=Label(Inv,text=f'x{sword3Count}',background='grey75')
                            if sword3State=='unlocked':
                                place(2,_.label,_.desc,_.title,_.equipButt,_.atkLab,_.crtLab,countLab)
                                if sword3Count==0:
                                    _.equipButt.config(state='disabled',text='Out of Item')
                            elif allUnlocked==True:
                                place(2,_.label,_.desc,_.title,_.equipButt,_.atkLab,_.crtLab,countLab)
                                if sword3Count==0:
                                    _.equipButt.config(state='disabled',text='Out of Item')
                            elif sword3State=='locked':
                                showLocked(50,200)
                            #show locked placeholder
            return _
        global sword2,currentWeapon,sword3
        sword2=createItem('sword','sword2',1,50,50,5,0,0,2,'C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\Misc\\sword2x64.png','An Orc\'s sword. Sharp, but flimsy.','Orc Sword')
        sword3=createItem('sword','sword3',2,500,500,3,0,0,1,'C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\Misc\\sword3x64.png','A slightly dull blade, but strong','Knight\'s sword')
        if currentWeapon=='sword2':
            sword1.equipButt.config(state='active',text='Equip')
            sword2.equipButt.config(state='disabled',text='Equipped')
            sword3.equipButt.config(state='active',text='Equip')
        if currentWeapon=='sword3':
            sword1.equipButt.config(state='active',text='Equip')
            sword3.equipButt.config(state='disabled',text='Equipped')
            sword2.equipButt.config(state='active',text='Equip')
        sword1.show()
        sword2.showInv()
        sword3.showInv()
        InvWin.mainloop()
#__________________________________________________________________________________________________________________________________________________  
    def openShop():
        shopWin=Tk()
        shopWin.geometry('500x500')
        Tk.title(shopWin,'Shop')
        shop=Canvas(shopWin,background='grey75',height=500,width=500)
        shop.pack()
        def back():
            shopButt.config(state='active')
            shopWin.destroy()
        def createShopItem(Id,Atk,Defense,Luck,Crt,SpriteFile,Desc,Title,Type):
            class _:
                #used to determine position on ui(word for tab, 0 for first, 5 for last)
                id=Id
                atk=Atk
                defense=Defense
                luck=Luck
                crt=Crt
                sprite=PhotoImage(master=shop,file=SpriteFile)
                label=Label(shop,image=sprite,highlightbackground='black',background='grey50',highlightthickness=1)
                label.photo=sprite
                desc=Label(shop,text=Desc,wraplength=150,height=4,width=20,highlightthickness=1,highlightbackground='black')
                title=Label(shop,text=Title,background='grey75')
                countLab=Label(shop,text=f'x{sword2Count}',background='grey75')
                def buy():
                    if Id=='sword3':
                        global sword3Count,sword3State
                        if sword3State=='locked':
                            sword3State='unlocked'
                        sword3Count=sword3Count+1
                        player.coins=player.coins-50
                        coins.set(player.coins)
                buyButt=Button(shop,text='Buy',command=buy)
                price=Label(shop,text='50 bucks')
                if Type=='sword':    
                    atkLab=Label(shop,text=f'+{atk} atk',foreground='red',background='grey75')
                    crtLab=Label(shop,text=f'+{crt} crt',foreground='#FF8E00',background='grey75')
                def showShop():
                    placeShop(0,_.label,_.desc,_.title,_.atkLab,_.crtLab,_.countLab)
            return _
        def placeShop(Pos:int,Item):
            if Pos==0:
                shop.create_window(50,60,window=Item.label)
                shop.create_window(170,60,window=Item.desc)
                shop.create_window(50,12,window=Item.title)
                shop.create_window(100,110,window=Item.atkLab)
                shop.create_window(135,110,window=Item.crtLab)
                shop.create_window(50,110,window=Item.buyButt)
                shop.create_window(50,145,window=Item.price)
            if Pos==1:
                shop.create_window(300,60,window=Item.label)
                shop.create_window(420,60,window=Item.desc)
                shop.create_window(300,12,window=Item.title)
                shop.create_window(350,110,window=Item.atkLab)
                shop.create_window(385,110,window=Item.crtLab)
                shop.create_window(300,110,window=Item.buyButt)
                shop.create_window(300,145,window=Item.price)
            if Pos==2:
                shop.create_window(50,200,window=Item.label)
                shop.create_window(170,200,window=Item.desc)
                shop.create_window(50,152,window=Item.title)
                shop.create_window(100,250,window=Item.atkLab)
                shop.create_window(135,250,window=Item.crtLab)
                shop.create_window(50,250,window=Item.buyButt)
                shop.create_window(50,285,window=Item.price)
        backButt=Button(shop,text='Back',command=back)
        sword3Shop=createShopItem('sword3',3,0,0,1,'C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\Misc\\sword3x64.png','A slightly dull, but strong sword.','Knight\'s Sword','sword')
        placeShop(0,sword3Shop)
        shop.create_window(250,450,window=backButt)
    def Qtown():
        global Turn
        Turn=50
        ModRPG.encounter()
    
    
    def yes():
        ModRPG.yes(mainCan,player,log,turn,coins)
    def no():
        ModRPG.no(mainCan,log,turn)
    def damage():
        ModRPG.damage(mainCan,player,log,Hp,HpStr,currentWeapon,turn2B,turn,levelText,xpDisplay,coins,sword2Count,sword2State)
    def bounce():
        ModRPG.bounce(mainCan,log,turn)
    def encounter():
        ModRPG.encounter(mainCan,log,attack,flee,monsterHp,HpLab,Hp,HpStr,yButt,nButt,shopButt,Turn)
    def HPChange():
        ModRPG.HPChange(mainCan,player,log)
    def manaChange():
        ModRPG.manaChange(mainCan,manaDisplay)
    def xpChange():
        ModRPG.xpChange(mainCan,player,log,levelText,xpDisplay)  
    def turn2():
        ModRPG.turn2(mainCan,log,attack,flee,dmgTaken,player) 
    #UI Elelments
    
    HpStr=StringVar()
    HpLab=Label(mainCan,textvariable=HpStr,background='grey75')
    Hp=IntVar()
    coins=StringVar(value='0')
    monsterHp=Progressbar(mainCan,length=75,variable=Hp)
    shopButt=Button(mainCan,text='Shop',command=openShop)
    #Dummy args because real ones arent defined
    yButt=Button(mainCan,text='Yes',command=yes)
    nButt=Button(mainCan,text='No',command=no)
    log=StringVar(value='No events have happened yet')
    attack=Button(mainCan,text='Attack',command=damage)
    flee=Button(mainCan,text='Flee',command=bounce)
    turn=Button(mainCan,text='Turn',command=encounter)
    instaTown=Button(mainCan,text='Go to nearest town',command=Qtown)
    butt=Button(mainCan, text='Hurt Yourself',width=12,height=2,command=HPChange)
    butt2=Button(mainCan, text='Cast',width=12,height=2,command=manaChange)
    levelText=StringVar(mainCan)
    butt3=Button(mainCan, text='Get xp for no reason',width=20,height=2,command=xpChange)
    level=Label(mainCan, textvariable=levelText,background='grey75',font=1)
    hpLabel=Label(mainCan,text='HP',background='grey75')
    manaLabel=Label(mainCan,text='Mana',background='grey75')
    xpLabel=Label(mainCan,text='XP',background='grey75')
    stats=Label(mainCan, text='Stats:')
    turn2B=Button(mainCan,text='Next Turn',command=turn2)
    invButt=Button(mainCan,image=ModRPG.invSprite,command=openInv)
    
    #Stat Displays
    atkStr=StringVar(value='Atk: 2')
    defStr=StringVar(value='Def: 1')
    lukStr=StringVar(value='Luk: 1')
    crtStr=StringVar(value='Crt: 1')
    
    
    logLabel=Label(mainCan,textvariable=log,highlightbackground='black',highlightthickness=1)
    atkLabel=Label(mainCan,textvariable=atkStr,background='grey75',foreground='red')
    defLabel=Label(mainCan,textvariable=defStr,background='grey75',foreground='blue')
    lukLabel=Label(mainCan,textvariable=lukStr,background='grey75',foreground='green')
    crtLabel=Label(mainCan,textvariable=crtStr,background='grey75',foreground='#FF8E00')
    coinsLab=Label(mainCan,textvariable=coins,background='grey75')
    butt.config(font=(40))
    butt2.config(font=(50))
    butt3.config(font=(2))
    levelText.set('Level: 1')
    #Display UI Elements
    if debugMode==1:    
        mainCan.create_window(450,250,window=butt)
        mainCan.create_window(250,250,window=butt2)
        mainCan.create_window(150,100,window=butt3)
        mainCan.create_window(50,200,window=UnlockButt)
        mainCan.create_window(50,250,window=give1Butt)
        mainCan.create_window(50,300,window=instaTown)
    mainCan.create_window(450,50,window=level)
    mainCan.create_window(50,562,window=hpLabel)
    mainCan.create_window(50,487,window=manaLabel)
    mainCan.create_window(50,412,window=xpLabel)
    mainCan.create_window(450,150,window=crtLabel)
    mainCan.create_window(450,130,window=lukLabel)
    mainCan.create_window(450,110,window=defLabel)
    mainCan.create_window(450,90,window=atkLabel)
    mainCan.create_window(350,30,window=logLabel)
    mainCan.create_window(350,190,window=turn,tags='turn')
    mainCan.create_window(80,160,window=coinsLab)
    mainCan.create_window(70,325,window=invButt)
    canWin.mainloop()