now=$(date +'%Y%m%d')

#./clarkrtem.sh
#timeout 1200 python3 broker.py

cat *.txt > proxy_$now.txt
sort -n proxy_$now.txt | uniq > proxy_"$now"_u.txt

python3 simple_test.py &
python3 simple_test_anycast.py &
python3 simple_test_httpbin.py &
python3 simple_test_revised.py &
python3 simple_test_anycast_revised.py &
python3 simple_test_httpbin_revised.py &
python3 simple_test_ebay_revised.py &
python3 simple_test_craigslist_revised.py &
python3 simple_test_bbc_revised.py


echo 'test finished!'
echo 'done!'
