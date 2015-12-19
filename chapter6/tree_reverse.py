def tree_reverse(l):
    r = []
    n = len(l) - 1
    i = 0
    while n >= 0:
        r.append(l[n])
        n -= 1
        i += 1
    return r
print tree_reverse([1, 2, [3,[4, 5],6]])
