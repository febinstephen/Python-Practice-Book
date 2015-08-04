#compare to strings ignoring the case
def istrcmp(a,b):
	a = a.upper()
	b = b.upper()
	if a == b:	
		return True
	else:
		return False
print istrcmp("l","atex")
	
