a,b=3,5
temp=a
a=b
b=temp
print(a)
print(b)
print("without using third variable")
a=a*b
b=a//b
a=a//b
print(a)
print(b)
print("type 3")
a=a+b
b=a-b
a=a-b
print(a)
print(b)
print("type 4")
a=a^b
b=a^b
a=a^b
print(a)
print(b)
a, b = 3, 5
print("Original values:", a, b)

# Swap using a list
temp = [a, b]
a, b = temp[1], temp[0]

print("Swapped values:", a, b)
a, b = 3, 5
print("Original values:", a, b)

# Swap using a list
temp = [a, b]
a, b = temp[1], temp[0]

print("Swapped values:", a, b)