a = [1,2,3]
b = [3,3,3,2,4]
#zip function
output = [(a[i],b[i]) for i in range(min(len(a),len(b)))]
print output
