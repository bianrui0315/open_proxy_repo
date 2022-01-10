#-*- coding: utf-8 -*-
import sys,os
try:
    import requests,readline
except ModuleNotFoundError:
    os.system('apt install readline && python -m pip install requests')
        
from core.library import library as _
from core.library import host_search as hs
from core.tmp import menu,logo
from core.tmp import R,G,B,Y,W

class execute(_,hs):

      def __init__(
                  self,
                  host,
                  method,
                  delay,
                  ):
          self.host = host
          self.method = method
          self.delay = delay

      @property    
      def search_proxy(self):
          _x = _._get_proxy()
          for i in range(len(_x['proxy'])):
              super().__init__(
              _x['proxy'][i],
              _x['port'][i].replace('<td>','').replace('</td>',''),
              self.host,
              self.method,
              self.delay,
              country=_x['country'][i],
              level=_x['level'][i],
              )
              super().check()

      @staticmethod        
      def host_search(domain):
          num = 0
          for i in hs(domain).request():
              num += 1
              print(f'{Y}{num}{W} - {i}')

      @classmethod
      def random_proxy(self):
          r = requests.get('https://api.getproxylist.com/proxy').json()
          print('\n')
          print(f'+ Proxy:Port :{G} {r.get("ip")}:{r.get("port")}{W}')
          print(f'+ Protocol   :{G} {r.get("protocol")}{W}')
          print(f'+ Country    :{G} {r.get("country")}{W}')
          print(f'+ Anonimity  :{G} {r.get("anonymity")}{W}')
          print(f'+ UpTime     :{G} {r.get("uptime")}{W} ')
          print(f'+ Download Speed :{G} {r.get("downloadSpeed")}{W}')
          print('\n')


print(logo)
print(menu)
while True:
      try:
         x = str(input(f'[G/{R}Tools{W}]: '))
         if x == '1':
            print(f'\n{G}[+]{W} Example : www.google.com\n')
            host = str(input('Host : '))
            if host == '':
               host = 'www.google.com'
            print(f'{G}\nCONNECT\nGET\nPOST\nTRACE\nPUT\nHEAD\nOPTIONS\nPATCH\nPROPATCH\nDELETE\nMOVE\n{W}')
            print(f'\n{Y}[!]{W} Type Enter if default CONNECT\n')
            method = str(input('Method : ')).upper()
            if method == '':
               method = 'CONNECT'
            print(f'\n{Y}[!]{W} Type Enter If default 5\n')
            delay = str(input('set Timeout : '))
            if delay == '':
               delay = '5'
            execute(host,method,int(delay)).search_proxy            
         elif x == '2':
              print(f'\n{B}[+]{W} Example : google.com\n')
              domain = str(input('Domain : '))
              print('\n')
              execute.host_search(domain)
              print('\n')
         elif x == '3':
              print('\n')
              execute.random_proxy()
              print('\n')
         elif x == '4':
              lst = []
              print('\n')
              _fp = str(input('Path-File : '))
              print('\n')
              host = str(input('Host : '))
              print(f'{G}\nCONNECT\nGET\nPOST\nTRACE\nPUT\nHEAD\nOPTIONS\nPATCH\nPROPATCH\nDELETE\nMOVE\n{W}')
              method = str(input('Method : ')).upper()
              with open(_fp) as pp:
                   for x in pp.readlines():
                       lst.append(x.split('\n')[0])
              for _pp in lst:
                  proxy,port = _pp.split(':')
                  _(
                    proxy,
                    int(port),
                    host,
                    method,
                    5
                    ).check()
         elif x == '5':
              print(f'\nExample :{Y} 0.0.0.0:8080{W}\n')
              proxy_port = str(input("Proxy:Port : "))
              if ':' not in proxy_port:
                  print(f'\n{R}[!]{W} Type must be 0.0.0.0:8080\n')
                  continue
              proxy,port = proxy_port.split(':')
              print('\nCONNECT\nGET\nPOST\nTRACE\nPUT\nHEAD\nOPTIONS\nPATCH\nPROPATCH\nDELETE\nMOVE\n')
              mtd = str(input('Method : ')).upper()
              _(proxy,port,str(input('Host : ')),mtd,5).check()
         elif x == '0':
              exit()
         else:
              print(f'\n{R}[x]{W} Number {x} Not Available\n')
      except FileNotFoundError as e:
         print(f'\n{R}[!]{W} {e}\n')
         continue
      except KeyboardInterrupt:
         break
      except EOFError:
         break










    
