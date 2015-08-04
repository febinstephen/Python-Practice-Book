import string
import os.path
def extsort(a):
	return sorted(a, cmp = lambda x, y: cmp(x.split(".")[1], y.split(".")[1]))
print extsort(["a.py","a.cxml","b.txt","b.py"])
