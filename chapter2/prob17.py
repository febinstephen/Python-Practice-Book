#program to print lines of a file in reverse order.
f = open("foo.txt",'r')
for i in reversed(f.readlines()):
	print i

