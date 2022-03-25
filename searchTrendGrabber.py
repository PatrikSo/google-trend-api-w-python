from pytrends.request import TrendReq
import pandas as pd
import csv

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["minecraft mod", "minecraft", "minecraft adventure map", "minecraft 100 days"] # list of keywords to get data
# topics to search ^^^
list_lists = ["rising","top"]
# result options ^^^
filterOption = ["images","news","youtube","froogle"] #default is Web Search
# gprop options ^^^

pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', gprop=filterOption[2]) 
data  = pytrends.related_queries()

#print(data['machine learning']['top'])
#print(data['minecraft']['top'])

#print(type(data['machine learning']))
#print(type(data['machine learning']['rising']))


#data[kw_list[0]][list_lists[0]].to_csv('ML rising trend.csv')

#print(len(data['machine learning']['rising']))

csvName = "{name} {types}.csv"
for num in range(len(kw_list)):
    print(kw_list[num])
    print(num)
    if data[kw_list[num]][list_lists[0]] is None:
        print('Empty')
    else:
        data[kw_list[num]][list_lists[0]].to_csv(csvName.format(name=kw_list[num],types=list_lists[0]))
    
for num in range(len(kw_list)):
    print(kw_list[num])
    print(num)
    if data[kw_list[num]][list_lists[1]] is None:
        print('Empty')
    else:
        data[kw_list[num]][list_lists[1]].to_csv(csvName.format(name=kw_list[num],types=list_lists[1]))
