#Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
from sys import argv
script,filename = argv 
f = open(filename,'r')
b = []
b = f.readlines()
length = len(f.readlines())
head = 10
tail = 10
for i in range(head):
	print b[i],
print"*"*10
for j in range(tail):
	print b[length-1],
	length -= 1
