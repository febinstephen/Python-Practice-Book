import urllib
from sys import argv
script,url = argv
page = urllib.urlopen(url)
#print page.headers
content = page.read()
if url[-1] == '/':
	with open("index.html","w") as f:
		f.write(content)
else:
	with open('url',"w") as f:
		f.write(content)

