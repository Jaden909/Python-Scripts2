"""Custom Functions and Classes for ConRPG"""
import random
from tkinter import *

def start(mainCan:Canvas):    
    global monster1Render,invRender,slash00,slash01,slash02,slash03,slash04,slash05,slash06,slash07,invSprite
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
    slash00.photo=slash0
class monster1:
    hp=10
    maxHp=10
    defense=0
    attack=1
    drop1Rate=90 #% drop rate
    drop2Rate=1
    def drop1(log,sword2Count,sword2State):#orc sword
        sword2Count=sword2Count+1
        log.set('The Monster dropped an orc sword!')
        if sword2State=='locked':
            sword2State='unlocked'
    def drop2(log:StringVar):
        log.set("The monster dropped something so rare it doesn't have a use yet")
    def lootDrop(log,sword2Count,sword2State):
        roll=random.choice(range(100))
        if roll<=monster1.drop1Rate:
            monster1.drop1(log,sword2Count,sword2State)
        if roll==monster1.drop2Rate:
            monster1.drop2()  
def slash(slashNum,mainCan:Canvas):
    mainCan.delete('slash')
    mainCan.create_window(410,100,window=slashNum,tags='slash')
def SwordSlash(mainCan:Canvas):
    mainCan.create_window(300,300,window=slash00,tags='slash')
    mainCan.after(50,slash(slash01,mainCan))
    mainCan.update()
    mainCan.after(50,slash(slash02,mainCan))
    mainCan.update()
    mainCan.after(50,slash(slash03,mainCan))
    mainCan.update()
    mainCan.after(50,slash(slash04,mainCan))
    mainCan.update()
    mainCan.after(50,slash(slash05,mainCan))
    mainCan.update()
    mainCan.after(50,slash(slash06,mainCan))
    mainCan.update()
    mainCan.after(50,slash(slash07,mainCan))
    mainCan.update()
    mainCan.after(50,mainCan.delete('slash'))
def yes(mainCan:Canvas,player,log:StringVar,turn:Button,coins:StringVar):
    if event=='wallet':
        coin=random.choice(range(100))*player.level
        log.set(f'Awesome! You found {coin} coins!')
        player.coins=player.coins+coin
        coins.set(player.coins)
        mainCan.create_window(350,190,window=turn,tag='turn')
        mainCan.delete('yn')  
def no(mainCan:Canvas,log:StringVar,turn:Button):
    if event=='wallet':
        log.set('You leave the wallet behind. The previous owner was probaly poorer than you anyway...')
        mainCan.create_window(350,190,window=turn,tag='turn')
        mainCan.delete('yn')
def encounter(mainCan:Canvas,log:StringVar,attack:Button,flee:Button,monsterHp,HpLab,Hp,HpStr,yButt,nButt,shopButt,Turn):
    global event
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
def coinUpdate(player,coins):
    coins.set(f'{player.coins}')
def monsterDamage(monster,player):
    global dmgTaken
    dmgTaken=random.choice([monster.attack,monster.attack+1])-player.defense
    if dmgTaken<0:
        dmgTaken=0
    player.hp=player.hp-dmgTaken 
def turn2(mainCan:Canvas,log:StringVar,attack:Button,flee:Button,dmgTaken:int,player):
    log.set(f'The monster did {dmgTaken} damage to you!')
    mainCan.create_window(400,200,window=attack,tags='action')
    mainCan.create_window(500,200,window=flee,tags='action')
    mainCan.delete('turn2')
    HPChange(mainCan,player,log)
def monsterDeath(monster,mainCan:Canvas,player,log:StringVar,turn:Button,levelText,xpDisplay,coins,sword2Count,sword2State):
    log.set('The monster was defeated!')
    xpChange(mainCan,player,log,levelText,xpDisplay)
    mainCan.delete('action')
    mainCan.delete('turn2')
    mainCan.delete('monster')
    mainCan.delete('monsterHp')
    monster.hp=monster.maxHp
    player.coins=player.coins+1
    mainCan.create_window(350,190,window=turn,tag='turn')
    coinUpdate(player,coins)
    monster.lootDrop(log,sword2Count,sword2State)
def damage(mainCan:Canvas,player,log:StringVar,Hp,HpStr,currentWeapon,turn2B,turn,levelText,xpDisplay,coins,sword2Count,sword2State):
    mainCan.delete('action')
    damageAmt=random.choice([player.attack,player.attack+1,player.attack+2,player.attack-1])
    if damageAmt==0:
        damageAmt=1
    SwordSlash(mainCan)
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
    monsterDamage(monster1,player)
    mainCan.create_window(350,160,window=turn2B,tags='turn2')
    if monster1.hp>0: 
        log.set(f'The monster took {damageAmt} damage!')
        monsterDamage(monster1,player)
        mainCan.create_window(350,200,window=turn2B,tags='turn2')
    else:
        monsterDeath(monster1,mainCan,player,log,turn,levelText,xpDisplay,coins,sword2Count,sword2State)
        
def bounce(mainCan:Canvas,log:StringVar,turn:Button):
    log.set('You fled!')
    mainCan.delete('action')
    mainCan.create_window(350,190,window=turn,tag='turn')
def HPChange(mainCan:Canvas,player,log:StringVar):
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
def manaChange(mainCan:Canvas,manaDisplay):
    manaDisplay=manaDisplay-10
    if manaDisplay>=50:    
        mainCan.delete('mana')
        mainCan.create_rectangle(50,425,manaDisplay,475,fill='sky blue',tags='mana')
def xpChange(mainCan:Canvas,player,log:StringVar,levelText,xpDisplay):
    #XP Gain Rates

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
def resetItemStats(player):
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