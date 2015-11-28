from os import listdir
from os import walk
#from os.path import 
dirname = 'dir'
list = listdir(dirname)#lists everything in the directory
print list
f = []

for (dirpath,dirnames,filenames) in walk(dirname):
	f.extend(dirnames)#lists files only 
	break
print f
