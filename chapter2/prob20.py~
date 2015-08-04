#Implement unix command grep
from sys import argv
script,filename,pattern = argv
f = open(filename,'r')
lines = []
check = []
lines = f.readlines()
for i in range(len(lines)):
	check = lines[i].split(' ')
	for j in check:
		if j == pattern:
			print lines[i]
	check[:] = []


