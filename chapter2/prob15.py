#reimplement unique function implemented in the earlier examples using sets.
def unique_set(a):
	a = set(a)
	return list(a)
print unique_set([2,3,3,4,4])
