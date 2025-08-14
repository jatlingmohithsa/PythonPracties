# '''even or odd
#     & or >>and<< '''
# n=int(input(""))
# if n&1:
#     print("odd")
# else:
#     print("even")

#adding numbers without +
a,b=6,7
print(a-(-b))

while b!=0:
    carry=a&b
    a=a^b
    b=carry<<1
print(a)
print("#Arithematic operators")
a,b=2,3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print("#comparition operators")
a,b=0,9
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print("# bit wies operators")
a,b=8,9
print(a<b or a==b)
print(a<b and a==b)
print(not b)
a,b=9,8
print(b<<2)
print(b<<2)
print(a&b)
print(a|b)
print(a^b)

print("#membershio operators")
a={1,2,3,4}
b=a
print(4 in a)
print(5 not in a)

print("#identity operators")
print(b is a)
print (9 is not b)