'''
Author: Patrik Sokolowski
Trendalyzer! Grabs Google Trend data on youtube given a keyword
reports data on said keyword
useful trend analysis?
'''
from pytrends.request import TrendReq
from tkinter import *
import pandas as pd
import csv


pytrends = TrendReq(hl='en-US', tz=360)                                                                 #ready the payload
kw_list = [" "]                                                                                         #keyword list
filterOption = ["images","news","youtube","froogle"]                                                    #filter keys for types of trend data to access

WIDTH=500
HEIGHT=300

data = []                                                                                               #data to be saved in payload


def rising_searches_related(data):
    '''
    Function takes payload data and prints the rising sub-category in a new window
    '''
    open_new_window("Rising Related Searches",data[kw_list[0]]['rising'])
    print('related rising searches queried')

def top_searches_related(data):
    '''
    Function takes payload data and prints the top sub-category in a new window
    '''
    open_new_window("Top Related Searches",data[kw_list[0]]['top'])
    print('related top searches queried')

def related_topics_top():
    '''
    Function prints related top topics and posts in new window
    '''
    open_new_window("Related Topics [top]", pytrends.related_topics()[str(kw_list[0])]['top'])
    print('related top topics queried')

def related_topics_rising():
    '''
    Function prints related rising topics and posts in new window
    '''
    open_new_window("Related Topics [rising]", pytrends.related_topics()[str(kw_list[0])]['rising'])
    print('related rising topics queried')

def suggested_items():
    '''
    Function prints suggested items based off keyword to new window
    '''
    open_new_window("Suggested Items", pytrends.suggestions(kw_list[0]))
    print('suggested items queried')

def historical_hourly_interest():
    '''
    Function prints historical context of keyword in new window
    '''
    open_new_window("Suggested Items", pytrends.get_historical_interest(kw_list[0],
                                                                        year_start=2022,
                                                                        month_start=1,
                                                                        day_start=1,
                                                                        hour_start=0,
                                                                        year_end=2022, month_end=2,
                                                                        day_end=1,
                                                                        hour_end=0,
                                                                        cat=0,
                                                                        geo='',
                                                                        gprop='',
                                                                        sleep=10))
    print('keyword historical context queried')


def click():
    '''
    Function gets called when SUBMIT button pressed, pulls keyword payload and runs other windows
    '''
    entered_text = textentry.get()
    kw_list[0] = str(entered_text)
    pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m') 
    data  = pytrends.related_queries()
    print(kw_list[0])
    rising_searches_related(data)
    top_searches_related(data)
    related_topics_top()
    related_topics_rising()
    suggested_items()
    historical_hourly_interest()
    print('Submitted Query with Keyword!')

window = Tk()                                                                                                   #main window, entry window with submit button setup!
window.title("window1")
lbl = Label(window, text="Enter a Keyword!", fg="black", font="none 12 bold")
lbl.grid(row=1, column=0, sticky=W)
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)


def open_new_window(name, txt):
    '''
    Function gets called by above functions to setup a new window for easy data showing
    '''
    window2 = Toplevel()
    window2.title(name)
    lbl = Label(window2, text=txt, fg="black", font="none 12 bold")
    lbl.grid(row=1, column=0, sticky=W)

window.mainloop()                                                                                               #end of main window lifespan


'''
v0.0.0
played with pytrends

v0.0.1
made main functionality
basic entry window
basic query of keyword

v0.0.2
adding more query features in new windows

'''
