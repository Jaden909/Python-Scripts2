"""_____________________________________________________________IDEAS____________________________________________________________________________""" 
#Tomorow:
#Stats/XP
#Saturday:
#Monsters/Quests
#Event Log
#Sunday:
#Trading/Shop/Gold
#Inventory/Items

#Settings

#if hp%10:
    #hpDisplay=(hp%10)*50

import random
from tkinter import *
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
    attack=1
    defense=1
    luck=1
    critChance=1
    coins=0
#Title Screen
mainWin=Tk()
Tk.title(mainWin,'ConRPG')
def startGame():
    global mainWin
    mainWin.destroy()
    global gameStarted
    gameStarted=1
mainWin.geometry('600x600')
pic=PhotoImage(file='C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\ConRPG\\assets\\logo\\LOGOMED.png',master=mainWin)
label=Label(mainWin)
label['image']=pic
title=Label(mainWin,text='ConRPG')
title.config(font=(50))
startB=Button(mainWin, text='Start',command=startGame,height=3,width=25)
startB.config(font=(50))
label.pack()
title.pack()
startB.pack()
mainWin.mainloop()
#Game code
if gameStarted==1:
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
    
    class monster1:
        hp=10
        defense=0
        attack=1
    def encounter():
        log.set('A monster appeared!')
        mainCan.create_window(400,200,window=attack,tags='action')
        mainCan.create_window(400,150,window=flee,tags='action')
    def coinUpdate():
        coins.set(f'{player.coins}')

    def monsterDamage(monster):
        global dmgTaken
        dmgTaken=random.choice([monster.attack,monster.attack+1])
        player.hp=player.hp-dmgTaken
        
    def turn2():
        log.set(f'The monster did {dmgTaken} damage to you!')
        mainCan.create_window(400,200,window=attack,tags='action')
        mainCan.create_window(400,150,window=flee,tags='action')
        mainCan.delete('turn2')
        HPChange()
    def damage():
        mainCan.delete('action')
        damageAmt=random.choice([player.attack,player.attack+1,player.attack+2,player.attack-1])
        monster1.hp=monster1.hp-damageAmt
        monsterDamage(monster1)
        mainCan.create_window(350,160,window=turn2B,tags='turn2')
        if monster1.hp>0: 
            log.set(f'The monster took {damageAmt} damage! It has {monster1.hp} hp left!')
            monsterDamage(monster1)
            mainCan.create_window(350,160,window=turn2B,tags='turn2')
        else:
            log.set('The monster was defeated!')
            xpChange()
            mainCan.delete('action')
            mainCan.delete('turn2')
            monster1.hp=10
            player.coins=+1
            coinUpdate()

    def bounce():
        log.set('You fled!')
        mainCan.delete('action')
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
            player.attack=player.attack+1
            player.defense=player.defense+1
            player.luck=player.luck+1
            player.critChance=player.critChance+1
            atkStr.set(f'Atk: {player.attack}')
            defStr.set(f'Def: {player.defense}')
            lukStr.set(f'Luk: {player.luck}')
            crtStr.set(f'Crt: {player.critChance}')
            levelText.set(f'Level: {player.level}')
            log.set('You leveled up! +1 to all stats')
            player.hp=50
            HPChange()
    #UI Elelments
    
    
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
    #Stat Displays
    atkStr=StringVar(value='Atk: 1')
    defStr=StringVar(value='Def: 1')
    lukStr=StringVar(value='Luk: 1')
    crtStr=StringVar(value='Crt: 1')
    log=StringVar(value='No events have happened yet')
    coins=StringVar(value='0')
    logLabel=Label(mainCan,textvariable=log)
    atkLabel=Label(mainCan,textvariable=atkStr,background='grey75',foreground='red')
    defLabel=Label(mainCan,textvariable=defStr,background='grey75',foreground='blue')
    lukLabel=Label(mainCan,textvariable=lukStr,background='grey75',foreground='green')
    crtLabel=Label(mainCan,textvariable=crtStr,background='grey75',foreground='orange')
    coinsLab=Label(mainCan,textvariable=coins,background='grey75')
    butt.config(font=(40))
    butt2.config(font=(50))
    butt3.config(font=(2))
    levelText.set('Level: 1')
    #Display UI Elements
    mainCan.create_window(450,250,window=butt)
    mainCan.create_window(250,250,window=butt2)
    mainCan.create_window(150,100,window=butt3)
    mainCan.create_window(450,50,window=level)
    mainCan.create_window(50,562,window=hpLabel)
    mainCan.create_window(50,487,window=manaLabel)
    mainCan.create_window(50,412,window=xpLabel)
    mainCan.create_window(450,150,window=crtLabel)
    mainCan.create_window(450,130,window=lukLabel)
    mainCan.create_window(450,110,window=defLabel)
    mainCan.create_window(450,90,window=atkLabel)
    mainCan.create_window(350,30,window=logLabel)
    mainCan.create_window(350,190,window=turn,tag='turn')
    mainCan.create_window(80,160,window=coinsLab)
    canWin.mainloop()