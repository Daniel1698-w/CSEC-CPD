y,w=map(int,input().split())

m=7-max(y,w)

if m==6:
    print("1/1")
elif m==1 or m==5:
    print(str(m)+"/"+'6')
elif m%2==0:
    print(str(m//2)+"/"+'3')
else:
    print('1/2')