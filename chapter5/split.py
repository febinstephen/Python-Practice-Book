import sys
filename  = sys.argv[1]
n = int(sys.argv[2]) 
print n
f = open(filename,'r')
i = 1 
for line in f.readlines():
    if (i % n == 0):
        new_file = open('split','w')
        new_file.write(line)
    else:
        new_file = open('opop','w')
        new_file.write(line)
    i += 1

