#a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import sys
filename = sys.argv[1]
k = int(sys.argv[2])
f = open(filename).readlines()
for i in f:
	new = i
	while len(new) > k:
		print new[:k]
		new = new[k:]
		print new
		break 






