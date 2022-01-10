from bs4 import BeautifulSoup as BS
import requests
import datetime
x = datetime.datetime.now().strftime("%Y%m%d%H%M")

text_proxy_daily=''
url="https://proxy-daily.com"
response=requests.get(url)
soup=BS(response.text,'lxml')
#print(soup.prettify())
proxies=soup.find_all(attrs={"class":"centeredProxyList freeProxyStyle"})
#text=soup.find_all('pre')
#print(text[-1].string)
#print(text[0].string)
for i in proxies:
	#print(i.text)
	text_proxy_daily+=str(i.text)+'\n'

#print(type(text))

with open('proxy_daily_'+x+'.txt','w') as f:
	f.write(text_proxy_daily)
