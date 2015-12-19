from os import walk
def findFiles(dirname):
	f = []
	print(dirname)
	for (dirpath, dirnames, filenames) in walk(dirname):
		f.extend(filenames)
	couter = 0
	for i in f:
		s = ''
		s = i.split('.')
		if 'py' in s:
			couter += 1
		print"%s\t"%i
	print couter
	d = []
	d.extend(dirpath)
	#print(d)
	#if len(d) != 0:
	#	for i in d:
	#		findFiles(i)
findFiles('dir')



