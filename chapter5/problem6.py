import os
for root,dirpath,filenames in os.walk(os.getcwd()):
    l = 0
    for i in filenames:
        if '.py' in i:
            for f in open(i):
                if f[0] not in ['#','\n']:
                    l += 1
print"Total length:",l
