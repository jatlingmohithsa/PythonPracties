r=int(input())
c=int(input())
tree=int(input())

if tree<1 or tree>r*c:
    print("No")
else:
    row=(tree-1)//c+1
    col=(tree-1)%c+1
    if row==1 or col==1 or col==c:
        print("Yes")
    else:
        print("No")
