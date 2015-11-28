from os import walk
from sys import argv
script,directory = argv
filesext = []
ext = []
dict1 = {}
for (dirpath,dirnames,filenames) in walk(directory):
	filesext.extend(filenames)
for i in filesext:
	ext = i.split('.')
	dict1[ext[1]] = dict1.get(ext[1],0)+1
	print ext
for key,values in dict1.items():
	print key,values
 
	
