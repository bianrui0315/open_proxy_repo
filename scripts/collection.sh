#!/bin/bash
date_current=`date '+%Y_%m_%d'`
datetime=`date '+%Y_%m_%d_%H_%M'`

filename1="./clarketm_$datetime.txt"
filename2="./rudnkh_$datetime.txt"
curl "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt" > $filename1
curl https://proxy.rudnkh.me/txt> $filename2
curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt | tail -n+3 > socks5_$datetime.txt
curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt | tail -n+3 > socks4_$datetime.txt
curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt   | tail -n+3 > http_$datetime.txt
curl https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt > opsxcq_$datetime.txt
python3 fate0.py
python3 test_proxy-daily.py
python3 test_proxylistdaily.py
python3 test_smallseotools.py
python3 dailyproxy.py
python3 sinium.py
python3 proxy-list.py
timeout 3000 python3 G-Tool_CONNECT.py &
timeout 3000 python3 G-Tool_GET.py &
timeout 3000 python3 broker.py > broker_$datetime.txt

echo date_current
echo 'done!'
