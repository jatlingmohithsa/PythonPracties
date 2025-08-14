a=int(input())
b=int(input())
c=int(input())
if(a<b and a<c):
    print("L1")
elif (b<a and b<c):
    print("L2")
else:
    print("L3")

#logic 2
r=min(a,b,c) # Using MIN funtion
if r==a:
    print("L1")
elif r==b:
    print("L2")
else:
    print("L3")

