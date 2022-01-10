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
	TEST_URL="https://httpbin.org/get"
	VALID_STATUS_CODES = [200,204,205,203,202,201,206,207,208,226]
	conn = aiohttp.TCPConnector(verify_ssl=False)
	async with aiohttp.ClientSession(connector=conn) as session:
		try:
			http_proxy  = 'http://' + proxy
			https_proxy = 'https://' + proxy
			print('testing', proxy)
			start=time.time()
			async with session.get(TEST_URL, proxy=http_proxy, timeout=15, allow_redirects=False) as response:
				if response.status in VALID_STATUS_CODES:
					status_code=str(response.status)
					#self.redis.max(proxy)
					end_1=time.time()
					print('valid', proxy)
					html = await response.text()
					headers=dict(response.headers)
					end_2=time.time()
					response_time=round(end_1-start,3)
					fetch_time=round(end_2-start,3)
					print(html)
					with open('proxy_usable_content_all_'+x+'_httpbin_new.txt','a') as us:
						us.write(proxy+'\n#####\n'+status_code+'\n#####\n'+str(headers)+'\n#####\n'+str(response_time)+'\n'+str(fetch_time)+'\n#####\n'+html+'\n*****\n')
				else:
					#self.redis.decrease(proxy)
					print('non-valid ', response.status, 'IP', proxy)
					#with open('proxy_statuscodeerror_all.txt','a') as ce:
					#	ce.write("%s\t%d\n" %(proxy,response.status))
		except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
			#self.redis.decrease(proxy)
			print('request failed', proxy)
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
		print('tester error', e.args)

run()
