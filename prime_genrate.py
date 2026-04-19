import math
def primes (n):
    boundery= int( n*( math.log(n)+ math.log(math.log(n))))
    print(boundery)
    lis= [True] * (boundery+1)
    lis[0]=lis[1]=False
    prime=[]
    count=0

    for i in range(2,int(boundery**0.5)+1):
        if lis[i]:
            for j in range(2*i, boundery+1,i):
                lis[j]=False
    
    for i in range(boundery+1):
        if count>=n:
            break
        if lis[i]:
            prime.append(i)
            count+=1
    print(len(prime))
    return prime
n=int(input())
print(primes(n))



