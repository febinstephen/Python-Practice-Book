#duplicate elements in a list
def die(k):
	k += 1
def dups(a):
	b = []
	for i in a:#iterate over 'a'
		count = 0
		for j in a:#iterate over 'b'
			if i == j:
				count = count+1
			else:
				die(0)
		if count >= 2:
		
			b.append(a[i])
		else:
			die(0)
	x= set(b) 
	print x
dups([1,5,2,3,3,5,5,5])

	

