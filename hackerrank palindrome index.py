def palindromeIndex(s):
    l=len(s)
    t=l-1
    for i in range(l//2):
        if s[i] is not s[t]:
            if s[i] is not s[i+1]:
                return i
            else:
                return t
        t-=1
    return -1
