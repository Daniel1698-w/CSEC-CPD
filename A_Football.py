from collections import defaultdict
n=int(input())
di=defaultdict(int)
for _ in range(n):
    s=input()
    di[s]+=1
_max= max(di.values())
for key, value in di.items():
    if value==_max:
        print(key)