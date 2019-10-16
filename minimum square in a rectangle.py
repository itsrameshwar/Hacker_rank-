def min_sq(a,b):
    if a==b:
        return 1
    elif a>b:
        return 1+min_sq(a-b,b)
    else:
        return 1+min_sq(a,b-a)
print(min_sq(11,1))
