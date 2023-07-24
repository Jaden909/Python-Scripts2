import random
import json 
from customtkinter import StringVar, IntVar,CTk,CTkSwitch
from customtkinter import CTkButton as Button
from customtkinter import CTkLabel as Label
from customtkinter import CTkCheckBox as Checkbutton
from customtkinter import CTkProgressBar as Progressbar
from tkinter import PhotoImage,Canvas
from tkinter import Label as OldLabel
from tkinter.ttk import Progressbar


gameStarted=0
#Title Screen
mainWin=CTk()
mainWin.title('Project: Price Hike v0.2DEV')
mainWin.geometry('300x300')
def startGame():
    global mainWin,gameStarted
    mainWin.destroy()
    gameStarted=1

#Setting toggles
debugMode=IntVar(value=0)
speedrunMode=IntVar(value=0)
debugToggle=CTkSwitch(mainWin,text='Debug Mode',variable=debugMode)
speedrunToggle=CTkSwitch(mainWin,text='Speedrun Mode',variable=speedrunMode)
#Image
pic=PhotoImage(master=mainWin,file='Assets\\Logo\\icon.png')
label=Label(mainWin,image=pic)

title=Label(mainWin,text='Project: Price Hike')

startB=Button(mainWin, text='Start',command=startGame,height=5,width=50)

ver0=Label(mainWin,text='Project: Price Hike v0.2 ALPHA DEV')

label.pack(pady=5)
title.pack()
startB.pack(pady=5)
debugToggle.pack(pady=10)
speedrunToggle.pack()
ver0.pack(pady=30)
mainWin.mainloop()
#Game code

if gameStarted==1:
    hpDisplay=600
    manaDisplay=600
    xpDisplay=75
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
    #Load Assets____________________________________________________________________________________________________________________
    currentWeapon='sword1'
    canWin=CTk()
    canWin.geometry('600x600')
    canWin.title('Project: Price Hike v0.2DEV')
    canWin.configure(cursor='tcross')
    mainCan=Canvas(canWin, width=700,height=700, background='grey25')
    mainCan.pack(pady=40)
    #HP Bar
    mainCan.create_rectangle(75,575,600,625,fill='grey60')
    mainCan.create_rectangle(75,575,hpDisplay,625,fill='light green',tags='hp')
    #Mana Bar
    mainCan.create_rectangle(75,475,600,525,fill='grey60')
    mainCan.create_rectangle(75,475,manaDisplay,525,fill='sky blue',tags='mana')
    #XP Bar
    mainCan.create_rectangle(75,375,600,425,fill='grey60')
    mainCan.create_rectangle(75,375,xpDisplay,425,fill='#eded68',tags='xp') 

    #mainCan.create_oval(50,150,70,170,fill='yellow')
    
    monster1Sprite=PhotoImage(file='Assets\\Monster1\\monster1_64.png')
    monster1Render=Label(mainCan,image=monster1Sprite,bg_color='grey25')

    invSprite=PhotoImage(file='Assets\\Inv\\Inv.png')
    invRender=Label(mainCan,image=invSprite,bg_color='grey25')
    
    coinSprite=PhotoImage(file='Assets\\Coin\\Coin.png')
    coinRender=Label(mainCan,image=coinSprite,bg_color='grey25',width=40)

    #Load Slash Frames
    slash0=PhotoImage(file='Assets\\SwordSlash\\64x\\slash0.png',master=mainCan)
    slash1=PhotoImage(file='Assets\\SwordSlash\\64x\\slash1.png',master=mainCan)
    slash2=PhotoImage(file='Assets\\SwordSlash\\64x\\slash2.png',master=mainCan)
    slash3=PhotoImage(file='Assets\\SwordSlash\\64x\\slash3.png',master=mainCan)
    slash4=PhotoImage(file='Assets\\SwordSlash\\64x\\slash4.png',master=mainCan)
    slash5=PhotoImage(file='Assets\\SwordSlash\\64x\\slash5.png',master=mainCan)
    slash6=PhotoImage(file='Assets\\SwordSlash\\64x\\slash6.png',master=mainCan)
    slash7=PhotoImage(file='Assets\\SwordSlash\\64x\\slash7.png',master=mainCan)
    Rslash0=PhotoImage(file='Assets\\RustySlash\\64x\\slash0.png',master=mainCan)
    Rslash1=PhotoImage(file='Assets\\RustySlash\\64x\\slash1.png',master=mainCan)
    Rslash2=PhotoImage(file='Assets\\RustySlash\\64x\\slash2.png',master=mainCan)
    Rslash3=PhotoImage(file='Assets\\RustySlash\\64x\\slash3.png',master=mainCan)
    Rslash4=PhotoImage(file='Assets\\RustySlash\\64x\\slash4.png',master=mainCan)
    Rslash5=PhotoImage(file='Assets\\RustySlash\\64x\\slash5.png',master=mainCan)
    Rslash6=PhotoImage(file='Assets\\RustySlash\\64x\\slash6.png',master=mainCan)
    Rslash7=PhotoImage(file='Assets\\RustySlash\\64x\\slash7.png',master=mainCan)
    #End of asset Loading___________________________________________________________________________________________________________
    save={'playerObj':player,'unlocks':[],'counts':[{'sword2Count':0,'sword3Count':0}],'turn':0}
    def saveGame(saveSlot,save):
        with open(saveSlot,'w') as f:
            json.dump(save,f)
    def loadGame(saveSlot):
        with open(saveSlot) as f:
            json.load(f)
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
            roll=random.choice(range(1,101))
            if roll<=monster1.drop1Rate:
                monster1.drop1()
            if roll==monster1.drop2Rate:
                monster1.drop2()
    if speedrunMode.get():
        slashSpeed=25
    else:
        slashSpeed=50
    def slash(slashNum):
        mainCan.delete('slash')
        mainCan.create_image(450,100,image=slashNum,tags='slash')
    def SwordSlash(type='default'):
        global slashSpeed
        if type =='default':    
            mainCan.create_image(450,100,image=slash0,tags='slash')
            mainCan.after(slashSpeed,slash(slash1))
            mainCan.update()
            mainCan.after(slashSpeed,slash(slash2))
            mainCan.update()
            mainCan.after(slashSpeed,slash(slash3))
            mainCan.update()
            mainCan.after(slashSpeed,slash(slash4))
            mainCan.update()
            mainCan.after(slashSpeed,slash(slash5))
            mainCan.update()
            mainCan.after(slashSpeed,slash(slash6))
            mainCan.update()
            mainCan.after(slashSpeed,slash(slash7))
            mainCan.update()
            mainCan.after(slashSpeed,mainCan.delete('slash'))
            
        if type =='rusty':    
            mainCan.create_image(450,100,image=Rslash0,tags='slash')
            mainCan.after(slashSpeed,slash(Rslash1))
            mainCan.update()
            mainCan.after(slashSpeed,slash(Rslash2))
            mainCan.update()
            mainCan.after(slashSpeed,slash(Rslash3))
            mainCan.update()
            mainCan.after(slashSpeed,slash(Rslash4))
            mainCan.update()
            mainCan.after(slashSpeed,slash(Rslash5))
            mainCan.update()
            mainCan.after(slashSpeed,slash(Rslash6))
            mainCan.update()
            mainCan.after(slashSpeed,slash(Rslash7))
            mainCan.update()
            mainCan.after(slashSpeed,mainCan.delete('slash'))
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
            if speedrunMode.get():    
                mainCan.create_window(400,200,window=attack,tags='action')
                mainCan.create_window(460,200,window=flee,tags='action')
            else:
                mainCan.create_window(320,250,window=attack,tags='action')
                mainCan.create_window(390,250,window=flee,tags='action')
            mainCan.create_window(350,150,window=monsterHp,tags='monsterHp')
            mainCan.create_window(350,170,window=HpLab,tags='monsterHp')
            Hp.set(100)
            HpStr.set(f'Hp: {monster1.hp}')
        if event=='wallet':
            log.set('You found a wallet! Do you want to see whats inside?')
            if speedrunMode.get():    
                mainCan.create_window(350,200,window=yButt,tags='yn')
                mainCan.create_window(400,200,window=nButt,tags='yn')
            else:
                mainCan.create_window(325,250,window=yButt,tags='yn')
                mainCan.create_window(375,250,window=nButt,tags='yn')
        if event=='town1':
            log.set('You\'ve arrived at noob town!')
            mainCan.create_window(100,325,window=shopButt)
        Turn+=1
        print(Turn)
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
        if speedrunMode.get():    
            mainCan.create_window(400,200,window=attack,tags='action')
            mainCan.create_window(460,200,window=flee,tags='action')
        else:
            mainCan.create_window(320,250,window=attack,tags='action')
            mainCan.create_window(390,250,window=flee,tags='action')
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
        if currentWeapon=='sword2':    
            SwordSlash('rusty')
        if currentWeapon=='sword1' or currentWeapon=='sword3':
            SwordSlash()
        monster1.hp=monster1.hp-damageAmt
        Hp.set(monster1.hp*10)
        HpStr.set(f'Hp: {monster1.hp}')
        if currentWeapon=='sword2':
            global sword2, sword2Count
            sword2.dur=sword2.dur-1
            if sword2.dur==0:
                log.set('Your Sword Broke!')
                sword2Count-=1
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
        hpDisplay=player.hp*10+100 
        if player.hp>0:    
            mainCan.delete('hp')
            mainCan.create_rectangle(75,575,hpDisplay,625,fill='light green',tags='hp')
        else:
            mainCan.delete('hp')
            mainCan.create_rectangle(75,575,75,625,fill='light green',tags='hp')
            log.set('You Died!')
            mainCan.delete('turn')
            mainCan.delete('action')
            mainCan.delete('turn2')      
    def manaChange():
        global manaDisplay
        manaDisplay=manaDisplay-10
        if manaDisplay>=50:    
            mainCan.delete('mana')
            mainCan.create_rectangle(75,475,manaDisplay,525,fill='sky blue',tags='mana')
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

        if xpDisplay<650:
            mainCan.delete('xp')
            mainCan.create_rectangle(75,375,xpDisplay,425,fill='#eded68',tags='xp') 
        #Level Up Code
        if xpDisplay>=600:
            xpDisplay=75
            mainCan.delete('xp')
            mainCan.create_rectangle(75,375,xpDisplay,425,fill='#eded68',tags='xp') 
            player.level+=1
            player.BaseAtk+=1
            player.BaseDef+=1
            player.BaseLuk+=1
            player.BaseCrt+=1
            player.attack+=1
            player.defense+=1
            player.luck+=1
            player.critChance+=1
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

    UnlockButt=Button(mainCan,text='Unlock All',command=unlockAll,state='disabled',width=50)
    give1Butt=Button(mainCan,text='Give 1 all',command=giveAll,width=50)
    allUnlocked=False
    #____________________________________________________________Inventory_________________________________________________________________________
    #Inv Window
    def openInv():
        InvWin=CTk()
        CTk.title(InvWin,'Inventory')
        InvWin.geometry('500x500')
        Inv=Canvas(InvWin,width=600,height=600,background='grey25')
        Inv.pack(pady=10)
        def showLocked(x:float,y:float):    
            lockedImage=PhotoImage(master=Inv,file='Assets\\Misc\\unknownItemx64.png')
            lockedLabel=Label(Inv,image=lockedImage,width=50)
            lockedLabel.photo=lockedImage
            UnknownTitle=Label(Inv,text='Unknown Item',background='grey25',width=50)
            UnknownDesc=OldLabel(Inv,text="Unknown Item. Keep exploring to discover more items",wraplength=150,height=4,width=20,highlightthickness=1,highlightbackground='grey80',background='grey15',foreground='grey80')
            Inv.create_window(x-10,y+20,window=lockedLabel)
            Inv.create_window(x,y-41,window=UnknownTitle)
            Inv.create_window(x+120,y+20,window=UnknownDesc)
        def back():
            global UnlockButt
            invButt.configure(state='active')
            UnlockButt.configure(state='active')
            InvWin.destroy()
        global invButt
        invButt.configure(state='disabled')
        backButt=Button(Inv,text='Back',command=back)
        Inv.create_window(250,450,window=backButt)
        #CTKTabView for Multi-Tab(future)
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
            swordSprite=PhotoImage(master=Inv,file='Assets\\Misc\\swordx64.png')
            swordLabel=OldLabel(Inv,image=swordSprite,highlightbackground='black',background='grey40',highlightthickness=1)
            swordLabel.photo=swordSprite
            swordDesc=OldLabel(Inv,text="A basic sword for slaying basic monsters. Doesn't break",wraplength=150,height=4,width=20,highlightthickness=1,highlightbackground='grey80',background='grey15',foreground='grey80')
            swordTitle=Label(Inv,text='Basic Sword',background='grey75',width=1)
            atkLab=OldLabel(Inv,text=f'+{atk} atk',foreground='red',background='grey25')
            def equip():
                global currentWeapon
                currentWeapon='sword1'
                resetItemStats()
                player.attack=player.attack+sword1.atk
                sword1.equipButt.configure(state='disabled',text='Equipped')
                sword2.equipButt.configure(state='active',text='Equip')
                atkStr.set(f'Atk: {player.attack}')
            equipButt=Button(Inv,text='Equipped',command=equip,state='disabled',width=50)
            def show():
                Inv.create_window(50,75,window=sword1.swordLabel)
                Inv.create_window(180,81,window=sword1.swordDesc)
                Inv.create_window(60,19,window=sword1.swordTitle)
                Inv.create_window(60,145,window=sword1.equipButt)
                Inv.create_window(125,145,window=sword1.atkLab)
        def place(Pos:int,label:Label,desc:Label,Title:Label,equipButt:Button,atkLab:Label,crtLab:Label,countLab:Label):
            if Pos==0:
                Inv.create_window(50,60,window=label)
                Inv.create_window(180,81,window=desc)
                Inv.create_window(60,19,window=Title)
                Inv.create_window(60,145,window=equipButt)
                Inv.create_window(110,145,window=atkLab)
                Inv.create_window(160,145,window=crtLab)
                Inv.create_window(230,110,window=countLab)
            if Pos==1:
                Inv.create_window(340,80,window=label)
                Inv.create_window(470,80,window=desc)
                Inv.create_window(350,19,window=Title)
                Inv.create_window(340,150,window=equipButt)
                Inv.create_window(400,150,window=atkLab)
                Inv.create_window(450,150,window=crtLab)
                Inv.create_window(530,150,window=countLab)
            if Pos==2:
                Inv.create_window(50,240,window=label)
                Inv.create_window(180,241,window=desc)
                Inv.create_window(60,179,window=Title)
                Inv.create_window(40,310,window=equipButt)
                Inv.create_window(100,310,window=atkLab)
                Inv.create_window(150,310,window=crtLab)
                Inv.create_window(230,310,window=countLab)
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
                label=OldLabel(Inv,image=sprite,highlightbackground='black',background='grey40',highlightthickness=1,width=64)
                label.photo=sprite
                desc=OldLabel(Inv,text=Desc,wraplength=150,height=4,width=20,highlightthickness=1,highlightbackground='grey80',background='grey15',foreground='grey80')
                title=Label(Inv,text=Title,background='grey75',width=1)
                
                if Type=='sword':    
                    atkLab=OldLabel(Inv,text=f'+{atk} atk',foreground='red',background='grey25')
                    crtLab=OldLabel(Inv,text=f'+{crt} crt',foreground='#FF8E00',background='grey25')
                def equip():
                    if Type=='sword':    
                        global currentWeapon
                        currentWeapon=Id   
                        if Id=='sword2':
                            sword1.equipButt.configure(state='active',text='Equip')
                            sword3.equipButt.configure(state='active',text='Equip')
                        if Id=='sword3':
                            sword2.equipButt.configure(state='active',text='Equip')
                            sword1.equipButt.configure(state='active',text='Equip')
                    resetItemStats()
                    player.attack,player.critChance=player.attack+_.atk,player.critChance+_.crt
                    _.equipButt.configure(state='disabled',text='Equipped')
                    atkStr.set(f'Atk: {player.attack}')
                    crtStr.set(f'Crt: {player.critChance}')
                #State should usually be active
                equipButt=Button(Inv,text='Equip',command=equip,state='active',width=1)
                def showInv():
                    if Pos==1:
                        if Id=='sword2':    
                            countLab=Label(Inv,text=f'x{sword2Count}',background='grey75',width=1)
                            if sword2State=='unlocked':
                                place(1,_.label,_.desc,_.title,_.equipButt,_.atkLab,_.crtLab,countLab)
                                if sword2Count==0:
                                    _.equipButt.configure(state='disabled',text='Out of Item')
                            elif allUnlocked==True:
                                place(1,_.label,_.desc,_.title,_.equipButt,_.atkLab,_.crtLab,countLab)
                                if sword2Count==0:
                                    _.equipButt.configure(state='disabled',text='Out of Item')
                            elif sword2State=='locked':
                                showLocked(350,60)
                    if Pos==2:
                        if Id=='sword3':    
                            countLab=Label(Inv,text=f'x{sword3Count}',background='grey75',width=1)
                            if sword3State=='unlocked':
                                place(2,_.label,_.desc,_.title,_.equipButt,_.atkLab,_.crtLab,countLab)
                                if sword3Count==0:
                                    _.equipButt.configure(state='disabled',text='Out of Item')
                            elif allUnlocked==True:
                                place(2,_.label,_.desc,_.title,_.equipButt,_.atkLab,_.crtLab,countLab)
                                if sword3Count==0:
                                    _.equipButt.configure(state='disabled',text='Out of Item')
                            elif sword3State=='locked':
                                showLocked(60,220)
                            #show locked placeholder
            return _
        global sword2,currentWeapon,sword3
        sword2=createItem('sword','sword2',1,50,50,5,0,0,2,'Assets\\Misc\\sword2x64.png','An Orc\'s sword. Sharp, but flimsy.','Orc Sword')
        sword3=createItem('sword','sword3',2,500,500,3,0,0,1,'Assets\\Misc\\sword3x64.png','A slightly dull blade, but strong','Knight\'s sword')
        if currentWeapon=='sword2':
            sword1.equipButt.configure(state='active',text='Equip')
            sword2.equipButt.configure(state='disabled',text='Equipped')
            sword3.equipButt.configure(state='active',text='Equip')
        if currentWeapon=='sword3':
            sword1.equipButt.configure(state='active',text='Equip')
            sword3.equipButt.configure(state='disabled',text='Equipped')
            sword2.equipButt.configure(state='active',text='Equip')
        sword1.show()
        sword2.showInv()
        sword3.showInv()
        InvWin.mainloop()
#__________________________________________________________________________________________________________________________________________________  
    def openShop():
        shopWin=CTk()
        shopWin.geometry('500x500')
        CTk.title(shopWin,'Shop')
        shop=Canvas(shopWin,background='grey25',height=600,width=600)
        shop.pack()
        def back():
            shopButt.configure(state='active')
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
                label=OldLabel(shop,image=sprite,highlightbackground='black',background='grey40',highlightthickness=1)
                label.photo=sprite
                desc=OldLabel(shop,text=Desc,wraplength=150,height=4,width=20,highlightthickness=1,highlightbackground='grey80',background='grey15',foreground='grey80')
                title=Label(shop,text=Title,background='grey75',width=1)
                countLab=Label(shop,text=f'x{sword2Count}',background='grey75',width=1)
                def buy():
                    if Id=='sword3':
                        global sword3Count,sword3State
                        if sword3State=='locked':
                            sword3State='unlocked'
                        sword3Count=sword3Count+1
                        player.coins=player.coins-50
                        coins.set(player.coins)
                buyButt=Button(shop,text='Buy',command=buy,width=1)
                price=Label(shop,text='50 bucks',width=1)
                if Type=='sword':    
                    atkLab=OldLabel(shop,text=f'+{atk} atk',foreground='red',background='grey25')
                    crtLab=OldLabel(shop,text=f'+{crt} crt',foreground='#FF8E00',background='grey25')
                def showShop():
                    placeShop(0,_.label,_.desc,_.title,_.atkLab,_.crtLab,_.countLab)
            return _
        def placeShop(Pos:int,Item):
            if Pos==0:
                shop.create_window(50,80,window=Item.label)
                shop.create_window(180,81,window=Item.desc)
                shop.create_window(70,19,window=Item.title)
                shop.create_window(110,145,window=Item.atkLab)
                shop.create_window(160,145,window=Item.crtLab)
                shop.create_window(50,145,window=Item.buyButt)
                shop.create_window(230,145,window=Item.price)
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
        sword3Shop=createShopItem('sword3',3,0,0,1,'Assets\\Misc\\sword3x64.png','A slightly dull, but strong sword.','Knight\'s Sword','sword')
        placeShop(0,sword3Shop)
        shop.create_window(250,450,window=backButt)
        shopWin.mainloop()
    def Qtown():
        global Turn
        Turn=50
        encounter()
    #UI Elelments
    instaTown=Button(mainCan,text='Go to nearest town',command=Qtown,width=70)
    shopButt=Button(mainCan,text='Shop',command=openShop)
    yButt=Button(mainCan,text='Yes',command=yes,width=20)
    nButt=Button(mainCan,text='No',command=no,width=20)
    HpStr=StringVar()
    HpLab=Label(mainCan,textvariable=HpStr,bg_color='grey25')
    Hp=IntVar()
    monsterHp=Progressbar(mainCan,length=75,variable=Hp)
    butt=Button(mainCan, text='Hurt Yourself',command=HPChange,width=12,height=2)
    butt2=Button(mainCan, text='Cast', command=manaChange,width=12,height=2)
    butt3=Button(mainCan, text='Get xp for no reason', command=xpChange,width=20,height=2)
    levelText=StringVar(mainCan)
    level=Label(mainCan, textvariable=levelText,bg_color='grey25')
    hpLabel=Label(mainCan,text='HP',bg_color='grey25')
    manaLabel=Label(mainCan,text='Mana',bg_color='grey25')
    xpLabel=Label(mainCan,text='XP',bg_color='grey25')
    stats=Label(mainCan, text='Stats:')
    turn=Button(mainCan,text='Turn',command=encounter)
    attack=Button(mainCan,text='Attack',command=damage,width=20)
    flee=Button(mainCan,text='Flee',command=bounce,width=20)
    turn2B=Button(mainCan,text='Next Turn',command=turn2)
    invButt=Button(mainCan,image=invSprite,command=openInv,text=None,width=30)
    ver=Label(mainCan,text='Project: Price Hike v0.2 ALPHA DEV',bg_color='grey25')

    #Stat Displays
    atkStr=StringVar(value='Atk: 2')
    defStr=StringVar(value='Def: 1')
    lukStr=StringVar(value='Luk: 1')
    crtStr=StringVar(value='Crt: 1')
    log=StringVar(value='No events have happened yet')
    coins=StringVar(value='0')
    logLabel=OldLabel(mainCan,textvariable=log,highlightbackground='black',highlightthickness=2,background='grey35',foreground='white')
    atkLabel=Label(mainCan,textvariable=atkStr,background='grey75',text_color='red')
    defLabel=Label(mainCan,textvariable=defStr,background='grey75',text_color='blue')
    lukLabel=Label(mainCan,textvariable=lukStr,background='grey75',text_color='green')
    crtLabel=Label(mainCan,textvariable=crtStr,background='grey75',text_color='#FF8E00')
    coinsLab=Label(mainCan,textvariable=coins,background='grey75')
    butt.configure()
    butt2.configure()
    butt3.configure()
    levelText.set('Level: 1')
    #Display UI Elements
    if debugMode.get()==1:    
        mainCan.create_window(450,250,window=butt)
        mainCan.create_window(250,250,window=butt2)
        mainCan.create_window(150,100,window=butt3)
        mainCan.create_window(50,200,window=UnlockButt)
        mainCan.create_window(50,250,window=give1Butt)
        mainCan.create_window(80,300,window=instaTown)
    mainCan.create_window(600,50,window=level)
    mainCan.create_window(89,555,window=hpLabel)
    mainCan.create_window(95,455,window=manaLabel)
    mainCan.create_window(90,350,window=xpLabel)
    mainCan.create_window(600,190,window=crtLabel)
    mainCan.create_window(600,160,window=lukLabel)
    mainCan.create_window(600,130,window=defLabel)
    mainCan.create_window(600,100,window=atkLabel)
    mainCan.create_window(350,30,window=logLabel)
    mainCan.create_window(350,190,window=turn,tags='turn')
    mainCan.create_window(90,160,window=coinsLab)
    mainCan.create_window(200,300,window=invButt)
    mainCan.create_window(135,650,window=ver)
    mainCan.create_window(80,160,window=coinRender)
    #mainCan.create_image(300,300,image=slash0)
    canWin.mainloop()