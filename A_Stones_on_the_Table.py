n=int(input())
string=input()
remove=0

for i in range(1,n):
    if string[i]==string[i-1]:
        remove+=1

print(remove)