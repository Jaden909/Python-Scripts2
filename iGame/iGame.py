from customtkinter import *
from tkinter import *
import decimal
mainWin=CTk()
mainWin.geometry('600x600')
mainWin.title('iGame')
mainCan=CTkCanvas(master=mainWin,background='grey25',width=700,height=700)

mainCan.pack(pady=20)
water=0
ppl=decimal.Decimal(1.00)
baseDemand=1000
demand=decimal.Decimal(baseDemand/ppl)
money=0
def manualWater():
    global water
    water+=1   
    waterSV.set(f'Water: {water}L')
def sell():
    global money,ppl,water
    if water>0:    
        money+=ppl
        moneySV.set(f'Money: ${money}')
        water-=1
        waterSV.set(f'Water: {water}L')
    mainCan.after(round(demand),sell)
def increaseby01():
    global ppl,demand
    ppl+=decimal.Decimal(0.01)
    ppl=round(ppl,2)
    demand=decimal.Decimal(baseDemand*ppl)
    pplSV.set(f'Price/L: ${ppl}')
def increaseby10():
    global ppl,demand
    ppl+=decimal.Decimal(0.1)
    ppl=round(ppl,2)
    demand=decimal.Decimal(baseDemand*ppl)
    pplSV.set(f'Price/L: ${ppl}')
def decreaseby01():
    global ppl,demand
    if round(ppl,2)>0.01:   
        ppl-=decimal.Decimal(0.01)
        ppl=round(ppl,2)
        demand=decimal.Decimal(baseDemand*ppl)
        pplSV.set(f'Price/L: ${ppl}')
def decreaseby10():
    global ppl,demand
    if round(ppl,2)>0.10: 
        ppl-=decimal.Decimal(0.1) 
        ppl=round(ppl,2)
        demand=decimal.Decimal(baseDemand*ppl)   
        pplSV.set(f'Price/L: ${ppl}')
waterSV=StringVar(value='Water: 0L')
waterLab=Label(mainCan,textvariable=waterSV,background='grey25',foreground='white',font=('idk',15))
makeWater=CTkButton(mainCan, text='Scoop water out of a river',command=manualWater)
waterTitle=Label(mainCan,background='grey25',text='Water Production',font=('underline',20,'underline'),foreground='white')

pplSV=StringVar(value='Price/L: $1.00')
moneySV=StringVar(value=f'Money: ${money}')
shopTitle=Label(mainCan,background='grey25',text='Marketing',font=('underline',20,'underline'),foreground='white')
pplLab=Label(mainCan,textvariable=pplSV,background='grey25',foreground='white',font=('idk',15))
p01=CTkButton(mainCan,text='+$.01',command=increaseby01,width=10)
p10=CTkButton(mainCan,text='+$.10',command=increaseby10,width=10)
m01=CTkButton(mainCan,text='-$.01',command=decreaseby01,width=10)
m10=CTkButton(mainCan,text='-$.10',command=decreaseby10,width=10)
moneyLab=Label(mainCan,textvariable=moneySV,background='grey25',foreground='white',font=('idk',15))

mainCan.create_window(150,40,window=waterTitle)
mainCan.create_window(150,80,window=waterLab)
mainCan.create_window(150,120,window=makeWater)

mainCan.create_window(500,40,window=shopTitle)
mainCan.create_window(500,80,window=pplLab)
mainCan.create_window(535,120,window=p01)
mainCan.create_window(600,120,window=p10)
mainCan.create_window(470,120,window=m01)
mainCan.create_window(405,120,window=m10)
mainCan.create_window(500,180,window=moneyLab)
mainCan.after(round(demand),sell)
mainWin.mainloop()