#!/bin/bash
dateyesterday=$(date --date=' 1 days ago' '+%Y%m%d')
date
cat live_ip_$dateyesterday.txt |  while read output
do
    ping -c 3 "$output" >> live_ip_ping_$dateyesterday.txt
    if [ $? -eq 0 ]; then
    echo "node $output is up" 
    else
    echo "node $output is down"
    fi
done
