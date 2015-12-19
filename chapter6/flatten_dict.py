flatten = {}
temp = {}
def flatten_dict(a):
    temp = {}
    for x,y in a.items():
         temp = {} 
         if isinstance(y, dict):
            for i,j in y.items():
                temp[x+'.'+i] = j
            flatten_dict(temp)
         else:
             flatten[x] = y
    return flatten

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
