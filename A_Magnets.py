n=int(input())
x=input()
group=1
for i in range(n-1):
    curr=input()
    if curr!=x:
        group+=1
    x=curr
print(group)