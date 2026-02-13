s=input()
c=0
sm=0
for i in s:
    if i==i.upper():
        c+=1
    else:
        sm+=1
if c>sm:
    s=s.upper()
    print(s)
else:
    s=s.lower()
    print(s)