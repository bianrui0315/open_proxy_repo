from bs4 import BeautifulSoup as BS
import requests
import datetime
x = datetime.datetime.now().strftime("%y%m%d%H%M")

url="https://seopro.sinium.com/free-proxy-list"
response=requests.get(url)
soup=BS(response.text,'lxml')

proxies=soup.find_all(attrs={"id":"rawData"})

text=''
for i in proxies:
	text+=i.text+'\n'


with open('simum_'+x+'.txt','w') as f:
	f.write(str(text))
