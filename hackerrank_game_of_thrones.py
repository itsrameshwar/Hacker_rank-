def gameOfThrones(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    c=0
    for i in d.values():
        if i%2 is not 0:
            c+=1
        if c==2:
            return 'NO'
        
    return 'YES'
