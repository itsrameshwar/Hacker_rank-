print("enter two float numbers")
start=float(input())
end=float(input())
count=int(input("enter a +ve number"))
l=[start]
d=(end-start)/(count-1)

while count>1:
    start += d
    l.append(start)
    count-=1

print(l)
