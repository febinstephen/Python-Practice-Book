import os
def tot_numlines(x):
    l=0
    for path,y,z in os.walk(os.getcwd()):
        for i in z:
             if x in i:
                 print os.path.join(path,i),":-",len(open(i).readlines())
                 l+=len(open(i).readlines())
    print "Total:-",l
tot_numlines(".py")
