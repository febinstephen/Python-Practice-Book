# find the min and max element of a list
def max_min(a):
	min = a[0]
	max = a[0]
	for i in a:
		if  min >= i:
			min = i
		if  max <= i:
			max = i
	print"MIN:%r\nMAX:%r"%(min,max)
max_min([2,10,1])
		
