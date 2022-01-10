#!/bin/bash
dateyesterday=$(date --date=' 1 days ago' '+%Y%m%d')

date
cat live_proxy_$dateyesterday.txt |  while read output
do	
	echo "$output"
	echo "$output" >> curl_proxy_$dateyesterday.txt
    curl --connect-timeout 10 -x "$output" -L  http://udel.edu/~bianrui/proxy/5MB.zip -o test.bin -w "%{speed_download},%{size_download},%{time_total}" >> curl_proxy_$dateyesterday.txt
    echo  -e '\n----------' >> curl_proxy_$dateyesterday.txt

done
