n=int(input())
c=ord('A')
for i in range(1+n+1):
    for j in range(1+n+1):
        print(chr(c),end=" ")
        c+=1
    print()

