def sumXor(n):
    if n==0 or n==1:
        return 1
    b=str(bin(n))
    s=b[2:]
    c=s.count('0')
    return pow(2,c)
