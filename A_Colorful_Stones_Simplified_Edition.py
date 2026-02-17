s=input()
t=input()
counter=1

for i in t:
    if i==s[counter-1]:
        counter+=1
print(counter)