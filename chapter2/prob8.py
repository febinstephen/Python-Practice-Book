#cumulative sum of a list
def cum_sum(a):
	b = []
	b.append(a[0]) 
	s = a[0]
	for i in range(1,len(a)):
		s = s+a[i]
		b.append(s)
	print b
cum_sum([2,2,3])

	
	
