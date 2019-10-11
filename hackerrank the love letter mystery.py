# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    c=0
    l=len(s)
    t=len(s)-1
    for i in range(l//2):
        o1=ord(s[i])
        o2=ord(s[t])
        if o1>o2:
            c+=(o1-o2)
        else:
            c+=(o2-o1)
        t-=1
    return c
