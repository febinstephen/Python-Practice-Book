list1 = [1, 2, 3]
list2 = [4, 5, 6]
def izip(list1, list2):
    for i in range(len(list1)):
        print list1[i],list2[i]
izip(list1, list2)
