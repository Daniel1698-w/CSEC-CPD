for i in range(1,6):
    li=list(map(int,input().split()))
    if 1 in li:
        x=li.index(1)+1
        print(abs(x-3)+abs(i-3))