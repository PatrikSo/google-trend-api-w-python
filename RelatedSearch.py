from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["machine learning", "minecraft"] # list of keywords to get data 

pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') 
data  = pytrends.related_queries()

#print(data['machine learning']['top'])
#print(data['minecraft']['top'])

print(data['machine learning']['rising'])

