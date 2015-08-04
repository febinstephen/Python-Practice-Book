#sum function implementation for list of strings
def sum_of_list(a):
	sum = ''
	for i in range(len(a)):
		sum = sum+a[i]
	return sum
print sum_of_list(['x','y','z'])


