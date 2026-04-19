t=int(input())
di={}
for _ in range(t):
    s=input()
    if s not in di:
        di[s]=0
        print("OK")
    else:
        di[s]+=1
        print(s+str(di[s]))
