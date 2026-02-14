n=int(input())
li=list(map(int,input().split()))
move=1
l=0
r=n-1
sereja=0
dima=0

while l<=r:
    if move%2==1:
        sereja+=max(li[r],li[l])
    else:
        dima+=max(li[r],li[l])

    if li[r]>li[l]:
        r-=1
    else:
        l+=1
    move+=1
print(sereja,dima)