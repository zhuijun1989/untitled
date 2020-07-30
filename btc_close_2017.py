# from urllib.request import urlopen
import json
import requests

#json_url = "https://github.com/zhuijun1989/untitled/blob/master/btc_close_2017.json"
filename ='btc_close_2017.json'

#'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'


with open(filename)as f:
    btc_date = json.load(f)
for btc_dict in btc_date:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close =int(btc_dict['close'])
    print("{} is month {} week {},{},the close price is {} RMB".format(date,month,week,weekday,close))

#response = urlopen(json_url)
# req = requests.get(json_url)
#
# with open('btc_close_2017_request.json','w',encoding='utf-8') as f:
#     f.write(req.text)
# file_requests = req.json()