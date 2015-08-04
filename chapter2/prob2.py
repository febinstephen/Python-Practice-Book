#sum function implementation for lists
def sum_of_list(a):
	sum = 0
	for i in range(len(a)):
		sum = sum+a[i]
	return sum
print sum_of_list([1,1,4])


