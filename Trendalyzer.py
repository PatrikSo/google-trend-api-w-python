from pytrends.request import TrendReq
from tkinter import *
import pandas as pd
import csv

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = [" "]
filterOption = ["images","news","youtube","froogle"]

WIDTH=500
HEIGHT=300

def click():
    entered_text = textentry.get()
    kw_list[0] = str(entered_text)

window = Tk()
window.title("window1")
Label(window, text="Enter a Keyword!", fg="black", font="none 12 bold").grid(row=1, column=0, sticky=W)
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

def open_new_window(name):
    window2 = Tk()
    window2.title(name)
    lbl = Label(window2, text="Window 2!", fg="black", font="none 12 bold")
    lbl.grid(row=1, column=0, sticky=W)
    #window2 = Toplevel()
    #window.after(1000, open_new_window)
    
open_new_window("window2")

window.mainloop()

