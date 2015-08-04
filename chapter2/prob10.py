#unique elements in the list
def die(k):
	k += 1
def unique(a):
	for i in a:#iterate over 'a'
		count = 0
		for j in a:#iterate over 'b'
			if i == j:
				count = count+1
			else:
				die(0)
		if count >= 2:
		
			die(0)
		else:
			print i,
unique([1,5,2,3,3,5,5,5])

	

