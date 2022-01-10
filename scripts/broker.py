
import datetime
import asyncio

from proxybroker import Broker
x = datetime.datetime.now().strftime("%m%d%H%M")

async def save(proxies, filename):

    with open(filename, 'w') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            #proto = 'https' if 'HTTPS' in proxy.types else 'http'
            #row = '%s://%s:%d\n' % (proto, proxy.host, proxy.port)
            row = '%s:%d' % (proxy.host, proxy.port)
            print(row)
            f.write(row+'\n')


def main():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(
        broker.find(types=['HTTP', 'HTTPS'], limit = 10000),
        save(proxies, filename='proxies_broker_'+x+'.txt'),
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)


if __name__ == '__main__':
    main()
