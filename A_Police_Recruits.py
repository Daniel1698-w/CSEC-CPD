n=int(input())
li=list(map(int,input().split()))
police_available=0
untreated=0

for i in li:
    if police_available==0 and i==-1:
        untreated+=1
    elif i!=-1:
        police_available+=i
    else:
        police_available-=1

print(untreated)