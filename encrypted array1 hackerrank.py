n=int(input())
l=list(map(int,input().split()))
s=sum(l)//(n-1)
for i in l:
    print(s-i,end=" ")
