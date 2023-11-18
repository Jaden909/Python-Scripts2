debugMode=0
import random
from tkinter import *
from tkinter.ttk import Progressbar
hpDisplay=550
manaDisplay=550
xpDisplay=50
gameStarted=0
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
pic=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\Logo\\LOGOMED.png',master=mainWin)
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
    #Load Assets____________________________________________________________________________________________________________________
    currentWeapon='sword1'
    canWin=Tk()
    Tk.title(canWin,'ConRPG')
    mainCan=Canvas(canWin, width=600,height=600, background='grey75')
    mainCan.pack()
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
    
    monster1Sprite=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\Monster1\\monster1_64.png')
    monster1Render=Label(mainCan,image=monster1Sprite,background='grey75')
    monster1Render.photo=monster1Sprite

    invSprite=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\Inv\\Inv.png')
    invRender=Label(mainCan,image=invSprite,background='grey75')
    invRender.photo=invSprite
    #Load Slash Frames
    slash0=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\SwordSlash\\64x\\slash0.png',master=mainCan)
    slash1=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\SwordSlash\\64x\\slash1.png',master=mainCan)
    slash2=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\SwordSlash\\64x\\slash2.png',master=mainCan)
    slash3=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\SwordSlash\\64x\\slash3.png',master=mainCan)
    slash4=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\SwordSlash\\64x\\slash4.png',master=mainCan)
    slash5=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\SwordSlash\\64x\\slash5.png',master=mainCan)
    slash6=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\SwordSlash\\64x\\slash6.png',master=mainCan)
    slash7=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\Assets\\SwordSlash\\64x\\slash7.png',master=mainCan)
    slash00=Label(mainCan,background='grey75',image=slash0)
    slash01=Label(mainCan,background='grey75',image=slash1)
    slash02=Label(mainCan,background='grey75',image=slash2)
    slash03=Label(mainCan,background='grey75',image=slash3)
    slash04=Label(mainCan,background='grey75',image=slash4)
    slash05=Label(mainCan,background='grey75',image=slash5)
    slash06=Label(mainCan,background='grey75',image=slash6)
    slash07=Label(mainCan,background='grey75',image=slash7)
    slash01.photo=slash1
    slash02.photo=slash2
    slash03.photo=slash3
    slash04.photo=slash4
    slash05.photo=slash5
    slash06.photo=slash6
    slash07.photo=slash7
    #End of asset Loading___________________________________________________________________________________________________________
    sword2Count=0
    sword2State='locked'
    sword3Count=0
    sword3State='locked'
    Turn=0
    class monster1:
        hp=10
        maxHp=10
        defense=0
        attack=1
        drop1Rate=90 #% drop rate
        drop2Rate=1
        def drop1():#orc sword
            global sword2Count,sword2State
            sword2Count=sword2Count+1
            log.set('The Monster dropped an orc sword!')
            if sword2State=='locked':
                sword2State='unlocked'
        def drop2():
            log.set("The monster dropped something so rare it doesn't have a use yet")
        def lootDrop():
            roll=random.choice(range(100))
            if roll<=monster1.drop1Rate:
                monster1.drop1()
            if roll==monster1.drop2Rate:
                monster1.drop2()
    
    def slash(slashNum):
        mainCan.delete('slash')
        mainCan.create_window(410,100,window=slashNum,tags='slash')
    def SwordSlash():
        mainCan.create_window(300,300,window=slash00,tags='slash')
        mainCan.after(50,slash(slash01))
        mainCan.update()
        mainCan.after(50,slash(slash02))
        mainCan.update()
        mainCan.after(50,slash(slash03))
        mainCan.update()
        mainCan.after(50,slash(slash04))
        mainCan.update()
        mainCan.after(50,slash(slash05))
        mainCan.update()
        mainCan.after(50,slash(slash06))
        mainCan.update()
        mainCan.after(50,slash(slash07))
        mainCan.update()
        mainCan.after(50,mainCan.delete('slash'))
    def yes():
        global event
        if event=='wallet':
            coin=random.choice(range(100))*player.level
            log.set(f'Awesome! You found {coin} coins!')
            player.coins=player.coins+coin
            global coins
            coins.set(player.coins)
            mainCan.create_window(350,190,window=turn,tag='turn')
            mainCan.delete('yn')  
    def no():
        global event
        if event=='wallet':
            log.set('You leave the wallet behind. The previous owner was probaly poorer than you anyway...')
            mainCan.create_window(350,190,window=turn,tag='turn')
            mainCan.delete('yn')
    def encounter():
        global event,Turn
        event=random.choice(['monster1','wallet'])
        if Turn==50:
            event='town1'
        if event=='monster1':
            log.set('A monster appeared!')
            mainCan.create_window(350,100,window=monster1Render,tags='monster')
            mainCan.create_window(400,200,window=attack,tags='action')
            mainCan.create_window(500,200,window=flee,tags='action')
            mainCan.create_window(350,150,window=monsterHp,tags='monsterHp')
            mainCan.create_window(350,170,window=HpLab,tags='monsterHp')
            Hp.set(100)
            HpStr.set(f'Hp: {monster1.hp}')
        if event=='wallet':
            log.set('You found a wallet! Do you want to see whats inside?')
            mainCan.create_window(350,200,window=yButt,tags='yn')
            mainCan.create_window(400,200,window=nButt,tags='yn')
        if event=='town1':
            log.set('You\'ve arrived at noob town!')
            mainCan.create_window(100,325,window=shopButt)
        Turn=Turn+1
        mainCan.delete('turn')
    def coinUpdate():
        coins.set(f'{player.coins}')
    def monsterDamage(monster):
        global dmgTaken
        dmgTaken=random.choice([monster.attack,monster.attack+1])-player.defense
        if dmgTaken<0:
            dmgTaken=0
        player.hp=player.hp-dmgTaken 
    def turn2():
        log.set(f'The monster did {dmgTaken} damage to you!')
        mainCan.create_window(400,200,window=attack,tags='action')
        mainCan.create_window(500,200,window=flee,tags='action')
        mainCan.delete('turn2')
        HPChange()
    def monsterDeath(monster):
        log.set('The monster was defeated!')
        xpChange()
        mainCan.delete('action')
        mainCan.delete('turn2')
        mainCan.delete('monster')
        mainCan.delete('monsterHp')
        monster.hp=monster.maxHp
        player.coins=player.coins+1
        mainCan.create_window(350,190,window=turn,tag='turn')
        coinUpdate()
        monster.lootDrop()
    def damage():
        mainCan.delete('action')
        damageAmt=random.choice([player.attack,player.attack+1,player.attack+2,player.attack-1])
        if damageAmt==0:
            damageAmt=1
        SwordSlash()
        monster1.hp=monster1.hp-damageAmt
        Hp.set(monster1.hp*10)
        HpStr.set(f'Hp: {monster1.hp}')
        if currentWeapon=='sword2':
            global sword2
            sword2.dur=sword2.dur-1
            if sword2.dur==0:
                log.set('Your Sword Broke!')
                sword2Count=sword2Count-1
                if sword2Count==0:
                    resetItemStats()
        monsterDamage(monster1)
        mainCan.create_window(350,160,window=turn2B,tags='turn2')
        if monster1.hp>0: 
            log.set(f'The monster took {damageAmt} damage!')
            monsterDamage(monster1)
            mainCan.create_window(350,200,window=turn2B,tags='turn2')
        else:
            monsterDeath(monster1)
            
    def bounce():
        log.set('You fled!')
        mainCan.delete('action')
        mainCan.create_window(350,190,window=turn,tag='turn')
    def HPChange():
        global hpDisplay
        hpDisplay=player.hp*10+50 
        if player.hp>0:    
            mainCan.delete('hp')
            mainCan.create_rectangle(50,500,hpDisplay,550,fill='light green',tags='hp')
        else:
            mainCan.delete('hp')
            mainCan.create_rectangle(50,500,50,550,fill='light green',tags='hp')
            log.set('You Died!')
            mainCan.delete('turn')
            mainCan.delete('action')
            mainCan.delete('turn2')      
    def manaChange():
        global manaDisplay
        manaDisplay=manaDisplay-10
        if manaDisplay>=50:    
            mainCan.delete('mana')
            mainCan.create_rectangle(50,425,manaDisplay,475,fill='sky blue',tags='mana')
    def xpChange():
        #XP Gain Rates
        global xpDisplay
        if player.level==1:
            xpDisplay=xpDisplay+25
        if player.level==2:
            xpDisplay=xpDisplay+25-(player.level*1.5)
        if player.level==3:
            xpDisplay=xpDisplay+25-(player.level*2)                
        if player.level==4:
            xpDisplay=xpDisplay+25-(player.level*2)
        if player.level==5:
            xpDisplay=xpDisplay+25-(player.level*2)
        if player.level>5:
            xpDisplay=xpDisplay+25-(player.level*1.75)

        if xpDisplay<=600:
            mainCan.delete('xp')
            mainCan.create_rectangle(50,350,xpDisplay,400,fill='#eded68',tags='xp')
        #Level Up Code
        if xpDisplay>=550:
            xpDisplay=50
            mainCan.delete('xp')
            mainCan.create_rectangle(50,350,xpDisplay,400,fill='green',tags='xp')
            player.level=player.level+1
            player.BaseAtk=player.BaseAtk+1
            player.BaseDef=player.BaseDef+1
            player.BaseLuk=player.BaseLuk+1
            player.BaseCrt=player.BaseCrt+1
            atkStr.set(f'Atk: {player.attack}')
            defStr.set(f'Def: {player.defense}')
            lukStr.set(f'Luk: {player.luck}')
            crtStr.set(f'Crt: {player.critChance}')
            levelText.set(f'Level: {player.level}')
            log.set('You leveled up! +1 to all stats')
            player.hp=50
            HPChange()
    def resetItemStats():
        player.attack,player.defense,player.luck,player.critChance=player.BaseAtk,player.BaseDef,player.BaseLuk,player.BaseCrt
        global atkStr,defStr,lukStr,crtStr
        atkStr.set(f'Atk: {player.BaseAtk}')
        defStr.set(f'Def: {player.BaseDef}')
        lukStr.set(f'Luk: {player.BaseLuk}')
        crtStr.set(f'Crt: {player.BaseCrt}')
    def unlockAll():
        global allUnlocked
        allUnlocked=True
    def giveAll():
        global sword2Count,sword3Count
        sword2Count,sword3Count=sword2Count+1,sword3Count+1

    UnlockButt=Button(mainCan,text='Unlock All',command=unlockAll,state='disabled')
    give1Butt=Button(mainCan,text='Give 1 all',command=giveAll)
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
                resetItemStats()
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
                    resetItemStats()
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
        encounter()
    #UI Elelments
    instaTown=Button(mainCan,text='Go to nearest town',command=Qtown)
    shopButt=Button(mainCan,text='Shop',command=openShop)
    yButt=Button(mainCan,text='Yes',command=yes)
    nButt=Button(mainCan,text='No',command=no)
    HpStr=StringVar()
    HpLab=Label(mainCan,textvariable=HpStr,background='grey75')
    Hp=IntVar()
    monsterHp=Progressbar(mainCan,length=75,variable=Hp)
    butt=Button(mainCan, text='Hurt Yourself',command=HPChange,width=12,height=2)
    butt2=Button(mainCan, text='Cast', command=manaChange,width=12,height=2)
    butt3=Button(mainCan, text='Get xp for no reason', command=xpChange,width=20,height=2)
    levelText=StringVar(mainCan)
    level=Label(mainCan, textvariable=levelText,background='grey75',font=1)
    hpLabel=Label(mainCan,text='HP',background='grey75')
    manaLabel=Label(mainCan,text='Mana',background='grey75')
    xpLabel=Label(mainCan,text='XP',background='grey75')
    stats=Label(mainCan, text='Stats:')
    turn=Button(mainCan,text='Turn',command=encounter)
    attack=Button(mainCan,text='Attack',command=damage)
    flee=Button(mainCan,text='Flee',command=bounce)
    turn2B=Button(mainCan,text='Next Turn',command=turn2)
    invButt=Button(mainCan,image=invSprite,command=openInv)

    
    #Stat Displays
    atkStr=StringVar(value='Atk: 2')
    defStr=StringVar(value='Def: 1')
    lukStr=StringVar(value='Luk: 1')
    crtStr=StringVar(value='Crt: 1')
    log=StringVar(value='No events have happened yet')
    coins=StringVar(value='0')
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