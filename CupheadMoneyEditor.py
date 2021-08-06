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
Label(m, text='Money to use:').grid(row=1,padx=2)

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
		data['inventories']['playerOne']['money'] = int(valueM.get())
		data['inventories']['playerTwo']['money'] = int(valueM.get())
		f.seek(0)
		json.dump(data, f, indent=4)
		f.truncate()

Menu = Frame(m)
Menu.grid(row=3, columnspan=3)

A = Button(Menu, text ="Change Value", command = modifyMoney)
A.pack()

m.mainloop()
