import tkinter
from tkinter import filedialog
from tkinter import *
import os.path
import fileinput
import sys
import json

m=tkinter.Tk(screenName='CupheadMoneyEditor',  baseName='CHME',  className='chme',  useTk=1)

#set title
m.title('Cuphead Money Editor by FX')

#Entry where user enters new value
Label(m, text='Money to use: (0-44)').grid(row=1,padx=2)

#Add textbox for new value
valueM = Entry(m)
valueM.grid(row=1, column=1,padx=2)

def getSaveFile():
    #Get save file location
    homedir = homedir = os.path.expanduser("~")
    savefileloc = homedir+"\\AppData\\Roaming\\Cuphead\\"

    return filedialog.askopenfilename(initialdir = savefileloc,title = "Select file",filetypes = (("cuphead save file","*.sav"),))

def modifyMoney():
	with open(getSaveFile(), 'r+') as f:
		data = json.load(f)
		value = max(0, min(int(valueM.get()), 44))
		data['inventories']['playerOne']['money'] = value
		data['inventories']['playerTwo']['money'] = value
		f.seek(0)
		json.dump(data, f, indent=4)
		f.truncate()

Menu = Frame(m)
Menu.grid(row=3, columnspan=3)

A = Button(Menu, text ="Change Value", command = modifyMoney)
A.pack()

m.mainloop()
