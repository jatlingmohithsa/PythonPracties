l=[1,2,3]
m=[2,3]
n1,n2=0,0
for i in range (len(l)):
    n1=n1*10+l[i]
for j in range (len(m)):
     n2=n2 *10 + m[j]
print(n1*n2)
    