import time
import tkinter as tk
from tkinter import *

import pyautogui

root = Tk()
root.title("AFK-Cursor")
root.geometry("630x520")
root.configure(background='gray')
root.iconbitmap('./img/icon.ico')

status = False 
position = 1
time = 1

def cursorPosition(pos = 1):
    x, y = pyautogui.position()
    pyautogui.moveTo(x + pos, y + pos, duration=0)

def base():
    if status: 
        cursorPosition(position)
    root.after(time * 1000, base)

def positionPlus():
    global position
    if (position >= 1000):
        position = 1000
    else:
        position += 1
    positionTxt['text'] = position

def positionMinus():
    global position
    if (position <= 0):
        position = 0
    else:
        position -= 1
    positionTxt['text'] = position

def timePlus():
    global time
    if (time >= 1000):
        time = 1000
    else:
        time += 1
    timeTxt['text'] = time

def timeMinus():
    global time
    if (time <= 0):
        time = 0
    else:
        time -= 1
    timeTxt['text'] = time

def statusStart():
    global status
    status = True
    statusTxt['text'] = 'Start'

def statusStop():
    global status
    status = False
    statusTxt['text'] = 'Stop'

def reset():
    global status, position, time
    status = False
    position = 1
    time = 1
    statusTxt['text'] = 'Stop'
    positionTxt['text'] = 1
    timeTxt['text'] = 1

by = tk.Label(root, text="by kah3vich", font=50, bg='gray', fg='white')
by.place(x=15, y=485)

statusTxt = tk.Label(root, text="Stop", font=28, bg='gray', fg='white')
statusTxt.grid(column=1, row=0, padx=35, pady=15)

positionTxt = tk.Label(root, text=position, font=28, bg='gray', fg='white')
positionTxt.grid(column=1, row=1, padx=35, pady=15)

timeTxt = tk.Label(root, text=time, font=28, bg='gray', fg='white')
timeTxt.grid(column=1, row=2, padx=35, pady=15)

start = Button(text="Start", command=statusStart, fg="white", bg="green", border=0, width=15, height=5, font=28)
start.grid(column=0, row=0, padx=35, pady=15)

stop = Button(text="Stop", command=statusStop, fg="white", bg="red", border=0, width=15, height=5, font=28)
stop.grid(column=2, row=0, padx=35, pady=15)

plusPosition = Button(text="Position+", command=positionPlus, fg="white", bg="black", border=0, width=15, height=5, font=28)
plusPosition.grid(column=0, row=1, padx=35, pady=15)

minusPosition = Button(text="Position-", command=positionMinus, fg="white", bg="black", border=0, width=15, height=5, font=28)
minusPosition.grid(column=2, row=1, padx=35, pady=15)

plusTime = Button(text="Time+", command=timePlus, fg="white", bg="black", border=0, width=15, height=5, font=28)
plusTime.grid(column=0, row=2, padx=35, pady=15)

minusTime = Button(text="Time-", command=timeMinus, fg="white", bg="black", border=0, width=15, height=5, font=28)
minusTime.grid(column=2, row=2, padx=35, pady=15)

resetButton = Button(text="RESET", command=reset, fg="white", bg="black", border=0, width=15, height=5, font=28)
resetButton.grid(column=1, row=3, padx=35, pady=15)

root.after(time * 1000, base)
root.mainloop()
