#Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
html = "http://projecteuler.net/"
page = urlopen(html).read()
soup = BeautifulSoup(page)
for a in soup.findAll('a', href=True):
    print "Found the URL:%r"%a['href']
