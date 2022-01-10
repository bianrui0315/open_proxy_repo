from bs4 import BeautifulSoup as BS
import requests

url="https://www.dailyfreeproxy.com/2020/01/31-01-20-fresh-new-proxy-https-1940.html"
response=requests.get(url)
soup=BS(response.text,'lxml')
#print(soup.prettify())
proxies=soup.find_all(attrs={"class":"alt2"})
#text=soup.find_all('pre')
#print(text[-1].string)
#print(text[0].string)
text_daily=''
for i in proxies:
	text_daily+=i.text+'\n'


with open('dailyfreeproxy_0131.txt','w') as f:
	f.write(str(text_daily))

