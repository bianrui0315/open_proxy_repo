import requests
import datetime
x = datetime.datetime.now().strftime("%m%d%H%M")
#print(x)

url='https://raw.githubusercontent.com/dxxzst/free-proxy-list/master/README.md'

html=requests.get(url).text

#print(html)

lines=html.split('\n')

#print(len(lines))


l_entry=[]
for i in lines:
	if '|' in i:
		l_entry.append(i)
		
#print(l_entry[-1])

text=''

for j in l_entry[2:]:
	text+=':'.join(j.split('|')[1:3])+'\n'
	
#print(text)

with open('dxxzst_proxy_'+x+'.txt','w') as g:
	g.write(text)
