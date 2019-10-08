def binomial_number(n,k):
    if k > (n-k):
        k=n-k
    r=1
    for i in range(k):
        r=r*(n-i)
        r=r//(i+1)
    return r

def catalan(n):
    c=binomial_number(2*n,n)
    return c//(n+1)

for i in range(5):
    print(catalan(i),end=" ")