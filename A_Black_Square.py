a,b,c,d=map(int,input().split())
s=input()
print(a * s.count('1') + b * s.count('2') + c * s.count('3') + d * s.count('4'))