#reverse a list
def reverse_list(a):
	n = len(a)
	for i in range(len(a)):
		print a[n-1],
		n -= 1
reverse_list([1,2,3])
