#a program to print each line of a file in reverse order.
def reverse(filename):
	a = []
	b = []
	f = open(filename,'r')
	a = f.readlines()
	for i in a:
		b = i.split()
		for j in reversed(b):
			print j,
		print"*"*10
		b[:] = []
reverse('foo.txt')

