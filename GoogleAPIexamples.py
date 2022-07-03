from pytrends.request import TrendReq
import pandas as pd
import csv

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["minecraft"]
filterOption = ["images","news","youtube","froogle"] #default is Web Search

pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m') 
data  = pytrends.related_queries()

# Interest Over Time (Dataframe)
# pytrends.interest_over_time()

# Historical Hourly Interest (Dataframe)
# pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)

# Interest by region
# pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)

# Related Topics
# pytrends.related_topics()

# Related Queries
# pytrends.related_queries()

# Trending Searches
# pytrends.trending_searches(pn='united_states') # trending searches in real time for United States

# Realtime Search Trends
# pytrends.realtime_trending_searches(pn='US')

# TopCharts
# pytrends.top_charts(date, hl='en-US', tz=300, geo='GLOBAL')

# Suggestions
# pytrends.suggestions(keyword)

# Categories
# pytrends.categories()

print(pytrends.suggestions(kw_list[0]))
print("1----------------------------------------")
print(pytrends.top_charts(date=2021, hl='en-US', tz=300, geo='GLOBAL'))
print("2----------------------------------------")
print(pytrends.related_queries())
print("3----------------------------------------")
print(pytrends.trending_searches(pn='united_states'))
print("4----------------------------------------")
print(pytrends.related_topics()['minecraft'])
print("5----------------------------------------")
print(type(pytrends.related_topics()['minecraft']))
print("6----------------------------------------")
print(pytrends.related_topics().keys())
print("7----------------------------------------")
print(pytrends.related_topics()['minecraft'].keys())
print("8----------------------------------------")
print(pytrends.related_topics()['minecraft']['rising'])
#pytrends.related_topics()['minecraft']['rising'].to_csv('Minecraft Rising test.csv')
print("9----------------------------------------")
print(pytrends.related_topics()['minecraft']['top'])
#pytrends.related_topics()['minecraft']['top'].to_csv('Minecraft Top test.csv')
print("10----------------------------------------")
print(pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0))
print("11----------------------------------------")
