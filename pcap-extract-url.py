#!/usr/bin/env python

import dpkt
import sys

f = open(sys.argv[1], "r")
pcap = dpkt.pcap.Reader(f)
urls = [ ]
http_ports = [80, 8080] 
for timestamp, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    if tcp.__class__.__name__ == 'TCP':
        if tcp.dport in http_ports and len(tcp.data) > 0:
            try:
                http = dpkt.http.Request(tcp.data)
                urls.append(http.headers['host'] + http.uri)
		f = open('newoutput.txt','w')
            except Exception as e:
           	 print "\n"
print "The URL's extracted from the PCAP are: \n"
for url in urls:
	print >> f , url
	print url
f.close()
