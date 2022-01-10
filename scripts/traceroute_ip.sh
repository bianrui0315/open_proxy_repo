#!/bin/bash
dateyesterday=$(date --date=' 1 days ago' '+%Y%m%d')

date
cat live_ip_$dateyesterday.txt |  while read output
do
	echo "$output"
	echo "----------------------" >> ip_traceroute_$dateyesterday.txt
	echo "$output" >> ip_traceroute_$dateyesterday.txt
    traceroute "$output" >> ip_traceroute_$dateyesterday.txt

done
