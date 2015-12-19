import os
def findFiles(dirname):
	f = []
	print(dirname)
        f = os.listdir(dirname)
	couter = 0
	for i in f:
		s = ''
		s = i.split('.')
		if 'py' in s:
			couter += 1
		print"%s\t"%i
	print couter
findFiles('dir')
