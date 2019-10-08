import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    l=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                continue
            elif arr[i]+arr[j]==m:
                l.append(i+1)
                l.append(j+1)
                l.sort()
                return (str(l[0])+" "+str(l[1]))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        r=icecreamParlor(m, arr)
        print(r)

        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
