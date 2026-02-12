n=int(input())
counter=0
for i in range(n):
    li=list(map(int,input().split()))
    if li.count(1)>=2:
        counter+=1
print(counter)
