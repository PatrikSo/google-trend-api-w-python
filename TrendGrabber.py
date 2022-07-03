#connect to google

# connect to google 

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360) 

# build payload

kw_list = ["machine learning"] # list of keywords to get data 

pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') 

#1 Interest over Time
data = pytrends.interest_over_time() 
data = data.reset_index() 


import plotly.express as px

fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
#fig.show()

data  = pytrends.related_queries()

print(data['machine learning']['top'])

keywords = pytrends.suggestions(keyword='Business Intelligence')
#df = px.DataFrame(keywords)
print(keywords)

