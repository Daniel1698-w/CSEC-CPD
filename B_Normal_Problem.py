t=int(input())
for _ in range(t):
    s=input()
    ans=''
    for i in s:
        if i=='p':
            ans+="q"
        elif i=='q':
            ans+='p'
        else:
            ans+=i
    print(ans[::-1])