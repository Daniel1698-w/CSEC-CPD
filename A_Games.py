n=int(input())
home=[]
away=[]
counter=0

for i in range(n):
    a,b=map(int,input().split())
    home.append(a)
    away.append(b)

for i in home:
    counter+=away.count(i)
print(counter)