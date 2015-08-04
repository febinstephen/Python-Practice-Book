#enumerate fun
def enumerate_list(b):
	l = len(b)
	for i in range(l):
		print "%d\t%d\n"%(i,b[i])
enumerate_list(['a','b','c'])
