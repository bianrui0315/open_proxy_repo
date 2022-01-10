import re
from datetime import datetime, timedelta
#date_yesterday=datetime.strftime(datetime.now(), '%Y%m%d')
date_yesterday=datetime.strftime(datetime.now()-timedelta(1), '%Y%m%d')
with open('proxy_usable_content_all_'+date_yesterday+'.txt') as f:
	text=f.read()
	
proxies=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}',text)
proxies_u=list(set(proxies))
#print(proxies)
#print(len(proxies))


text_proxy=''
for proxy in proxies_u:
	text_proxy+=proxy+'\n'

ips=[]
ports=[]

for proxy in proxies_u:
	ip,port=proxy.split(':')
	ips.append(ip)
	ports.append(port)

ips_u=list(set(ips))
ports_u=list(set(ports))

text_ip=''
for ip in ips_u:
	text_ip+=ip+'\n'

text_ports=''
for port in ports_u:
	text_ports+=port+'\n'
	
	
with open('live_proxy_'+date_yesterday+'.txt','w') as pr:
	pr.write(text_proxy)
	
with open('live_ip_'+date_yesterday+'.txt','w') as pi:
	pi.write(text_ip)
	
with open('live_ports_'+date_yesterday+'.txt','w') as po:
	po.write(text_ports)
