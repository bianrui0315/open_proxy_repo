import requests
import datetime
import json

x = datetime.datetime.now().strftime("%m%d%H%M")
#print(x)

url='https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'

html=requests.get(url).text

#print(html)

lines=html.split('\n')

print(len(lines))
#print(lines[0])
#print(lines[-1])


#d=json.loads(lines[0])
#print(d["host"],":",d["port"])

'''
l_entry=[]
for i in lines:
	if '|' in i:
		l_entry.append(i)
		
#print(l_entry[-1])
'''
text=''

for j in lines[:-1]:
	#print(j)
	d=json.loads(j)
	text+=d["host"]+":"+str(d["port"])+'\n'
	
#print(text)

with open('fate0_proxy_'+x+'.txt','w') as g:
	g.write(text)

