#product function implementation for lists
def product_of_list(a):
	product = 1
	for i in range(len(a)):
		product = product*a[i]
	return product
print product_of_list([0,2,3])


