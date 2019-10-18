def funnyString(s):
    s1=s[::-1]
    l1,l2=[],[]
    for i in range(len(s)-1):
        l1.append(abs(ord(s[i])-ord(s[i+1])))
    for i in range(len(s)-1):
        l2.append(abs(ord(s1[i])-ord(s1[i+1])))
    for i in range(len(l1)):
        if l1[i] is not l2[i]: 
            return 'Not Funny'
    return 'Funny'
