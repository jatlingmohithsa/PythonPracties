c=int(input())
a,b=0,1
for i in range(2,c):
    c=a+b
    a=b
    b=c  
print("===",c)

print("Using while loop")
c = int(input("Enter the number of terms: "))
i, a, b = 0, 0, 1  

print("Fibonacci Series:")
while i < c:
    print(a, end=' ')  
    a, b = b, a + b   
    i += 1 
