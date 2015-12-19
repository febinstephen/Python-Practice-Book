def unflatten_dict(d):
    unflatten = {}
    temp = {}
    key =  []
    for x,y in d.items():
        lst = []
        if '.' in x:
             lst = x.split('.')
             if not lst[0] in key:
                key.append(lst[0])
             temp[lst[1]] = y
        else:
            unflatten[x] = y

    for i in key:
        unflatten[i] = temp
    return unflatten
print unflatten_dict({'a':1, 'b':2, 'c.x':3, 'c.y':4})
