from collections import defaultdict
t=int(input())

for _ in range(t):
    n=int(input())
    count=0
    di= defaultdict(int)
    li=list(map(int,input().split()))

    for i, val in enumerate(li):
        if di[val-i]:
            count+=di[val-i]
        di[val-i]+=1
    print(count)