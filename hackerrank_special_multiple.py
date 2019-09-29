def special_multiple(n):
    i=1
    while 1:
        s=bin(i)
        s=str(s)
        b=s[2:]
        b=int(b)
        b*=9
        if b%n==0:
            return b
        i+=1
print(special_multiple(7))
