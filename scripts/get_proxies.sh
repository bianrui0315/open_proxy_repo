#!/bin/bash
PATH=/home/rui/open_proxy/:/home/rui/bin:/home/rui/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/home/rui/traIXroute/bin:/snap/bin
datetime=`date '+%Y_%m_%d_%H_%M'`

date_current=`date '+%Y%m%d'`
cd /home/rui/open_proxy/
mkdir file_$date_current
cd file_$date_current

date_yesterday=`date --date="1 days ago" '+%Y%m%d'`
cp ../file_$date_yesterday/proxy_"$date_yesterday"_u.txt .

cp -r ~/Documents/proxy_scripts/* .

chmod 755 *

for (( i=1; i <= 4; i++ ))
do
	timeout 3600 ./collection.sh
done

./sort_uniq.sh

python3 get_proxy_and_IP.py
./ping_ip.sh &
./traceroute_ip.sh &
./curl_proxy.sh
