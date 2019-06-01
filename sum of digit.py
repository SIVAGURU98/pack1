#gurunathan
n=int(input())
summ=0
while n>0:
    print(n,end='')
    r=n%10
    print(r)
    summ=summ+r
    n=n//10
print('sum of the digits:',summ)

