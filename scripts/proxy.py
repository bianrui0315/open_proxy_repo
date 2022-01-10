from netaddr import *
import re
from pydnsbl import DNSBLChecker
from dns import reversename, resolver
from ipwhois import IPWhois
import pprint
import whois
import socket
import requests
import json
import glob
import os
import difflib
from geolite2 import geolite2



class Proxy():
	''' process proxy using ip, port'''
	
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		
	def check_if_microsoft(self):
		ipa=IPAddress(self.ip)
		with open('/home/rui/open_proxy/cloud/microsoft_ip_range.txt') as f:
			for line in f:
				parts=line.strip('\n').split('\t')
				if '.' in parts[0]:
					prefix=IPNetwork(parts[0])
					if ipa in prefix:
						return True

		return False
		
	def check_if_amazon(self):
		ipa=IPAddress(self.ip)
		with open('/home/rui/open_proxy/cloud/amazon_ip_range.txt') as f:
			for line in f:
				parts=line.strip('\n').split('\t')
				if '.' in parts[0]:
					prefix=IPNetwork(parts[0])
					if ipa in prefix:
						return True

		return False
		
	def check_if_google(self):
		ipa=IPAddress(self.ip)
		with open('/home/rui/open_proxy/cloud/google_ip_range.txt') as f:
			for line in f:
				parts=line.strip('\n').split('\t')
				if '.' in parts[0]:
					prefix=IPNetwork(parts[0])
					if ipa in prefix:
						return True

		return False
		
	def check_if_cloud(self):
		if self.check_if_microsoft() or self.check_if_amazon() or self.check_if_google():
			return True
		else:
			return False
			
	def check_amazon_region(self):
		ipa=IPAddress(self.ip)
		with open('/home/rui/open_proxy/cloud/amazon_ip_range.txt') as f:
			for line in f:
				parts=line.strip('\n').split('\t')
				if '.' in parts[0]:
					prefix=IPNetwork(parts[0])
					if ipa in prefix:
						return parts[1]

		return False
	def check_microsoft_region(self):
		ipa=IPAddress(self.ip)
		with open('/home/rui/open_proxy/cloud/microsoft_ip_range.txt') as f:
			for line in f:
				parts=line.strip('\n').split('\t')
				if '.' in parts[0]:
					prefix=IPNetwork(parts[0])
					if ipa in prefix:
						return parts[1]

		return False
		
	def if_BL(self):
		checker = DNSBLChecker()
		result = checker.check_ip(self.ip)	
		return result.blacklisted
	
	def BL_cat_det(self):
		checker = DNSBLChecker()
		result = checker.check_ip(self.ip)
		return result.categories,result.detected_by
		
	def rdns(self):
		
		try:
			rname=reversename.from_address(self.ip)
			r_dns=str(resolver.query(rname,"PTR")[0])
			return r_dns[:]
		except resolver.NXDOMAIN:
			return False
		
		#r_dns=socket.gethostbyaddr(self.ip)
		#return r_dns[0]	
	def IP_whois_info(self):
		obj=IPWhois(self.ip)
		res=obj.lookup_whois()
		return res
		
	def Domain_whois_info(self):
		try:
			res=whois.whois(self.rdns())
			return res
		except whois.parser.PywhoisError:
			return False
				
	def check_if_proxy_work(self):
		ip=self.ip
		port=self.port
		proxy=ip+':'+port
		proxies={'http':'http://'+proxy, 'https': 'https://'+proxy}
		try:	
			response=requests.get('http://udel.edu/~bianrui/proxy/proxy.html',proxies=proxies, timeout=10)
			return True
		except:
			return False
			
	def ratio_2html(self):
		ip=self.ip
		port=self.port
		proxy=ip+':'+port
		proxies={'http':'http://'+proxy, 'https': 'https://'+proxy}
		#url='http://udel.edu/~bianrui/proxy/proxy.html'
		url='http://cnn.com'
		response_origin=requests.get(url)
		response=requests.get(url,proxies=proxies,timeout=10)
		s=difflib.SequenceMatcher(None,response_origin.text,response.text)
		return(round(s.ratio(),3))
		
	def proxied_response(self):
		ip=self.ip
		port=self.port
		proxy=ip+':'+port
		proxies={'http':'http://'+proxy, 'https': 'https://'+proxy}
		url='http://udel.edu/~bianrui/proxy/proxy.html'
		response=requests.get(url,proxies=proxies,timeout=10)
		return(response.text)	
	
	def geo(self):
		reader = geolite2.reader()
		res=reader.get(self.ip)
		return res
'''		
proxy1=Proxy('198.199.122.218','8080')

print(proxy1.check_if_microsoft())
print(proxy1.check_if_amazon())
print(proxy1.check_if_google())
print(proxy1.check_if_cloud())
print(proxy1.check_amazon_region())
print(proxy1.if_BL())
print(proxy1.rdns())
print(proxy1.IP_whois_info()['asn_description'])
print(proxy1.Domain_whois_info())


print(proxy1.ratio_2html())
print(proxy1.geo()['country']['names']['en'])
'''
proxy_text=''
with open('proxy_ip_0924_u.txt') as f:
	for line in f:
		try:
			proxy=line.strip('\n')
			proxy_text+=proxy+'\t'
			print(proxy)
			proxy=Proxy(proxy,'')
			#print(proxy.rdns())
			#print(proxy.IP_whois_info()['asn_description'])
			print(proxy.geo()['country']['names']['en'])
			proxy_text+=str(proxy.geo()['country']['names']['en'])+'\n'
			#print(proxy.Domain_whois_info())
		except:
			proxy_text+='\n'
		
with open('proxy_ip_country_0924.txt','w') as ppp:
	ppp.write(proxy_text)
