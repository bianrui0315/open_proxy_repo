import asyncio
import aiohttp
import time
import sys
import datetime

x = datetime.datetime.now().strftime("%Y%m%d")

try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
#from proxypool.db import RedisClient
#from proxypool.setting import *



async def test_single_proxy(proxy):
	"""
	测试单个代理
	:param proxy:
	:return:
	"""
	
	#TEST_URL="http://www.google.com"
	TEST_URL="http://udel.edu/~bianrui/proxy/proxy.html"
	VALID_STATUS_CODES = [200,204,205,203,202]
	conn = aiohttp.TCPConnector(verify_ssl=False)
	async with aiohttp.ClientSession(connector=conn) as session:
		try:
			http_proxy  = 'http://' + proxy
			https_proxy = 'https://' + proxy
			print('正在测试', proxy)
			start=time.time()
			async with session.get(TEST_URL, proxy=http_proxy, timeout=15, allow_redirects=False) as response:
				if response.status in VALID_STATUS_CODES:
					#self.redis.max(proxy)
					end_1=time.time()
					print('代理可用', proxy)
					html = await response.text()
					end_2=time.time()
					response_time=round(end_1-start,3)
					fetch_time=round(end_2-start,3)
					print(html)
					with open('proxy_usable_content_all_'+x+'.txt','a') as us:
						us.write(proxy+'\n#####\n'+str(response_time)+'\n'+str(fetch_time)+'\n#####\n'+html+'\n#####\n')
				else:
					#self.redis.decrease(proxy)
					print('请求响应码不合法 ', response.status, 'IP', proxy)
					#with open('proxy_statuscodeerror_all.txt','a') as ce:
					#	ce.write("%s\t%d\n" %(proxy,response.status))
		except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
			#self.redis.decrease(proxy)
			print('代理请求失败', proxy)
			#with open('proxy_confail_all.txt','a') as cf:
			#	cf.write(proxy+'\n')
    
def run():
	"""
	测试主函数
	:return:
	"""
	BATCH_TEST_SIZE=100
        
	with open('proxy_'+x+'_u.txt') as f:
		text=f.read()
	proxies=text.split('\n')
	while '' in proxies:
		proxies.remove('')
		
	print('测试器开始运行')
	try:
		count = len(proxies)
		print('当前剩余', count, '个代理')
		for i in range(0, count, BATCH_TEST_SIZE):
			start = i
			stop = min(i + BATCH_TEST_SIZE, count)
			print('正在测试第', start + 1, '-', stop, '个代理')
			test_proxies = proxies[start: stop]
			loop = asyncio.get_event_loop()
			tasks = [test_single_proxy(proxy) for proxy in test_proxies]
			loop.run_until_complete(asyncio.wait(tasks))
			sys.stdout.flush()
			time.sleep(5)
	except Exception as e:
		print('测试器发生错误', e.args)

run()
