import json
import requests
info = {'weather_type':'forecast','location':'吉首','key':'39224f60a10a48aebc37f11110db23b7'}
url = 'https://free-api.heweather.net/s6/weather/{weather_type}?location={location}&key={key}'.format(**info)
response = requests.get(url).json()['HeWeather6'][0]
print('所在地区为'+response['basic']['location'])
print('经纬度为'+response['basic']['lat']+" "+response['basic']['lon'])
print('更新时间'+response['update']['loc'])
print("*"*30)
forecast = response['daily_forecast']
for i in forecast:
    print('预测日期'+i['date'])
    print('\t日出时间'+i['sr'])
    print('\t日落时间'+i['ss'])
    print('\t月出时间'+i['mr'])
    print('\t月落时间'+i['ms'])
    print('\t最高温度'+i['tmp_max'])
    print('\t最低'+i['tmp_min'])
    print('\t白天天气'+i['cond_txt_d'])
    print('\t晚间天气'+i['cond_txt_n'])
    print('\t降雨概率'+i['pop'])