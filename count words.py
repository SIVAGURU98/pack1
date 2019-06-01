#gurunathan
str=input()
c=0
for i in range(len(str)):
    r=i%10
    c=c+1
    i=i//10
print(c)

