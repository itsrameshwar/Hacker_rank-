a=[[1,2],[3,4],[4,5,[6,7]],8]
a=str(a)
list1=[]
for i in a:
    if i.isdigit():
        list1.append(int(i))
print(list1)



list=[[1,2,3],[4,5,6],[7,8,9]]                    #printing 2d list
print(list[0][0])
for i in list:
    print(*i)

##n=int(input())
##m=int(input())
##list=[]
##for i in range(n):                                #initialization of 2d list
##    temp=[]
##    for j in range(m):
##        temp.append(int(input("enter value of row i+1 column j+1")))
##    list.append(temp)
##
##print(list)

list=[1,2,3,4,5,6,7,8,9]
list1=[]
n=2
m=2
k=0
l=n
print(n,m)
for i in range(m):
    list1.append(list[k:l])
    k+=n
    l+=n
print(list1)
































