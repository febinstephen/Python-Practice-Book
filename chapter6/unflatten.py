def unflatten(dictionary):
   resultDict = { } 
   for key, value in dictionary.items():
       parts = key.split(".")
       d = resultDict 
       print d
       for part in parts[:-1]:
            if part not in d:
               d[part] = { }
            d = d[part]
       d[parts[-1]] = value
   return resultDict
print unflatten({'a':1, 'b.x':2, 'b.y':3, 'c': 4})
