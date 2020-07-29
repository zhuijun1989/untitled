from urllib.request import urlopen
import json

#json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
#response = urlopen(json_url)
#req = response.read()

with open('btc_close_2017.json','wb') as f:
    f.write(q)
    file_urllib = json.load(q)
print(file_urllib)
