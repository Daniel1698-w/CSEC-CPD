n,h=list(map(int,input().split()))
ai=list(map(int,input().split()))
w=0
for i in ai:
    if i<=h:
        w+=1
    else:
        w+=2
print(w)
