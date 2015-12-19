import os
import sys
f = open('file','r')
o = open('index','w')
for line  in f:
    if len(line) > 40:
        o.write(line)
