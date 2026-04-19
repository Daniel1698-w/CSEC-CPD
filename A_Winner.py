from collections import defaultdict
t=int(input())
di= {}
lis={}

for i in range(t): 
    name, score= map(str, input().split())
    score=int(score)
    if name not in  di:
        di[name]= [[score,i]]
        continue
    di[name].append([score, i])



_max=0 
# print(di)

for key, value in di.items(): 
    # print(f"key = {key} , value = {value}")
    _max=max(_max, sum(x[0] for x in value))


# print(f" max = {_max}")

for key , value in di.items(): 
    if sum(x[0] for x in value)== _max:
        lis[key]=  value


# print(f" lis = {lis}")

if len(lis)==1:
    for key in lis:
        print(key)

else:
    li={}

    for key, value in lis.items():
        _sum=0
        for val, indx in value:
            _sum+= val
            if _sum>= _max:
                li[indx]= key
                break
    _min= min( li)
    print(li[_min])