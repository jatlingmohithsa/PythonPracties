n=int(input())
a=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(a,end=" ")
            a+=1
        else:
            print(" ",end=" ")
    print()