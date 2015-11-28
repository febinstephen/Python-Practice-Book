from os import walk
from sys import argv
import os.path
script,directory = argv
files = []
for (dirpath,dirnames,filenames) in walk(directory):
	files.extend(filenames)
print"Filename\tSize\tLast Modified"
#print files
for f in files:
	f = os.path.join(directory,f)
	statbuf = os.stat(f)	
	#print i
	fil = open(f,'r')
	length = len(fil.read())
	#print length
	fil.close()
	print"%s\t%d\t%r"%(f,length,statbuf.st_mtime)
#print f.readline()
