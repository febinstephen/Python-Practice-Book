itr = iter(range(5))
def peep(itr):
    lst = []
    for i in itr:
        lst.append(i)
    return lst[0],lst
print peep(itr)
