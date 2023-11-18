import json,random,customtkinter,tkinter
mainWin=customtkinter.CTk()
mainWin.title('ConvoStarters')
mainWin.geometry('300x100')
choice=tkinter.Label(text='Click Generate',wraplength=300,font=20,background='grey14',foreground='white')
customtkinter.CTkButton(text='Generate',command=lambda:choice.config(text=random.choice(json.load(open('convostarters.json'))))).pack()
choice.pack(pady=10)
mainWin.mainloop()