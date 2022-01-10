from bs4 import BeautifulSoup as BS
import requests
import datetime
x = datetime.datetime.now().strftime("%y%m%d%H%M")

url="https://www.dailyfreeproxy.com/"
response=requests.get(url)
soup=BS(response.text,'lxml')
urls=soup.find_all('a', href=True)
for i in urls:
	if 'proxy-https' in i['href']:
		print(i['href'])
		url=i['href']
		break

response=requests.get(url)
soup2=BS(response.text,'lxml')
proxies=soup2.find_all(attrs={"class":"alt2"})
text_daily=''
for i in proxies:
	text_daily+=i.text+'\n'

with open('dailyfreeproxy_'+x+'.txt','w') as f:
	f.write(str(text_daily))

