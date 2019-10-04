def stringConstruction(s):
    c=0
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
            c+=1
    return c
