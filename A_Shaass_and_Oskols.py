n=int(input())
li=list(map(int,input().split()))
m=int(input())

for i in range(m):
    x,y=map(int,input().split())
    l=li[x-1]
    li[x-1]=0
    if x!=1:
        li[x-2]+=y-1
    if x!=n:
        li[x]+=l-y
        
for i in li:
    print(i)
