import pandas as pd
data = pd.read_excel('Location List.xls')
#print(data)

import json
from urllib.request import urlopen, quote
import requests
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '---'
    address = quote(address) 
    uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak 
    req = urlopen(uri)
    res = req.read().decode() 
    temp = json.loads(res)
    #print(temp)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lat,lng
    #return temp

   
for indexs in data.index:
    try:
        get_location = getlnglat(data.loc[indexs,'地址'])
        get_lat = get_location[0]
        get_lng = get_location[1]
        data.loc[indexs,'纬度'] = str(get_lat)
        data.loc[indexs,'经度'] = str(get_lng)
        data.loc[indexs,'经纬度'] = str(get_location)
        print(str(indexs)+'-'+str(get_lat)+'-'+str(get_lng))
    except:
        print(str(indexs)+'-'+'-')
        pass


print(data)


