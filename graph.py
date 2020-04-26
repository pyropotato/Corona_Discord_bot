import matplotlib.pyplot as plt
import datetime
import urllib3
import json
import random

http = urllib3.PoolManager()

response = http.request('GET','https://api.thevirustracker.com/free-api?countryTimeline=IN')
data = response.data #byte
data = data.decode('utf8') #converting byte to string
data = json.loads(data)
data = data['timelineitems'][0]
dates = list(data.keys())
values = []
for x in data.keys():
    if x != 'stat' :
        values.append(data[x]["total_cases"])
dates = dates[:len(dates) -1:]
fig = plt.figure(figsize = (40,8))
plt.plot(dates,values, color="#ff0000", linewidth=3)
plt.gcf().autofmt_xdate()
plt.grid()
plt.savefig('plt.png')