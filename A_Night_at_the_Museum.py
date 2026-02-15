name=input()
first=ord(name[0])
rotations=min(abs(first-ord('a')),123-first)

for i in range(1,len(name)):
    curr=ord(name[i])
    rotations += min( abs(curr-first), abs(122-first +(curr-96) if first>curr 
                                       else 122-curr+(first-96)) )
    first=curr

print(rotations)