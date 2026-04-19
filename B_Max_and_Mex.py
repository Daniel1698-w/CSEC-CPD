t=int(input())
import math

def mex(lis):
    i=0
    while i in lis:
        i+=1
    return i

for _ in range(t):
    n,k =map(int, input().split())
    lis=set(map(int,input().split()))
    _max= max(lis)
    Mex=mex(lis)
    if k==0:
        print(len(lis))
        continue
    if Mex > _max:
        print(len(lis)+k)
    else:
        val= (_max+Mex+1)//2
        print( len(lis)+ int(val not in lis ))