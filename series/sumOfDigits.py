# n=int(input())
# sum=0
# while n>0:
#     n1=n%10
#     sum+=n1
#     n//=10    
# print("sum of digits:",sum)

sum=0
n=int(input())
for i in range(0,len(str(n))):
    sum+=n%10
print("sum ",sum)
'''A program repeatedly sums the digits of a number until a single-digit result is obtained.

Input Format:
A single integer.
Output Format:
Print Single digit: X, where X is the result.
Sample Input:
Copy code
987
Sample Output:
Single digit: 6'''
