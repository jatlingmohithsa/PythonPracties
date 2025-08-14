n=int(input())
ls=[]
sum=0
for i in range(n):
    ls.append(int(input()))
sum=ls[0]
for i in range(1,n):
    sum=sum+ls[i]
print(sum)