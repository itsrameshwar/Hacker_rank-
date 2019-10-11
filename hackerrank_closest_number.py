def closestNumbers(arr):
    arr.sort()
    m=arr[1]-arr[0]
    l1=len(arr)
    l=[]
    for i in range(l1-1):
        if m>arr[i+1]-arr[i]:
            m=arr[i+1]-arr[i]
    for i in range(l1-1):
        if (arr[i+1]-arr[i])==m:
            m=arr[i+1]-arr[i]
            l.append(arr[i])
            l.append(arr[i+1])
    return l        
