import os
import sys
def tree(dirname, i=0):
    try:
        files = os.listdir(dirname)
        k = 0
        print ' '*i,dirname
        while k < len(files):
            if '.' in files[k]:
                print' '*i,'|' ' '*2,files[k] 
            else:
                tree(dirname+'/'+files[k], i+2)
            k = k+1
    except OSError:
        return
tree(sys.argv[1])
