import socket
from urllib import urlopen
url = "http://httpbin.org/get"
#page = urlopen(url).read()
#print page
print "LOCAL HOST=%s"% (urllib.localhost())
print "IP=%s"%(socket.gethostbyname(url))
