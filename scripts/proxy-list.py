from bs4 import BeautifulSoup as BS
import requests
import datetime
from selenium import webdriver
x = datetime.datetime.now().strftime("%m%d%H%M")

url="https://www.proxy-list.download/HTTP"
'''
response=requests.get(url)
soup=BS(response.text,'lxml')
#print(soup.prettify())
areas=soup.find_all(attrs={"class":"textarea"})
for i in areas:
	print(i.text)
	
#print(text_daily)
'''
'''
with open('dailyfreeproxy_'+x+'.txt','w') as f:
	f.write(str(text_daily))
'''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
#chrome_options.add_argument('window-size = 2400x1200')
chrome = webdriver.Chrome(options=chrome_options)
chrome.get(url)
#print(chrome.page_source)
button=chrome.find_element_by_id('downloadbtn')
button.click()
#print(aaa.text)
chrome.close()

