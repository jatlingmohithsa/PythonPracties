n=int(input)
l=len(int(n))
sum=0
a=n
while(n>0):
    r=n%10
    sum+=r**l
    n=n//10
if a==sum:
    print("armstrong") 
else:
    print("not armstrong")
    
    