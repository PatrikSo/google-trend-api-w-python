from pytrends.request import TrendReq
from tkinter import *
import pandas as pd
import csv

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = [" "]
filterOption = ["images","news","youtube","froogle"]

WIDTH=500
HEIGHT=300

data = []

'''
def interest_over_time():
    pytrends.interest_over_time()

def historical_hourly_interest():
    pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)
'''

def rising_searches_related(data):
    print(data[kw_list[0]]['rising'])
    #risingLBL = Label(window, text=data[kw_list[0]]['rising'], fg="black", font="none 12 bold")
    #risingLBL.grid(row=3, column=0, sticky=W)
    open_new_window("Rising Related Searches",data[kw_list[0]]['rising']) 

def top_searches_related(data):
    print(data[kw_list[0]]['top'])
    open_new_window("Top Related Searches",data[kw_list[0]]['top']) 

def click():
    entered_text = textentry.get()
    kw_list[0] = str(entered_text)
    pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m') 
    data  = pytrends.related_queries()
    print(kw_list[0])
    rising_searches_related(data)
    top_searches_related(data)

window = Tk()
window.title("window1")
lbl = Label(window, text="Enter a Keyword!", fg="black", font="none 12 bold")
lbl.grid(row=1, column=0, sticky=W)
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

def open_new_window(name, txt):
    window2 = Toplevel()
    window2.title(name)
    lbl = Label(window2, text=txt, fg="black", font="none 12 bold")
    lbl.grid(row=1, column=0, sticky=W)

window.mainloop()
