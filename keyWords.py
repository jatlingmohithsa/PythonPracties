import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
#   'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
#     'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

a=20
print(a)
print(f"(a:5)")

b=10
c=10,0.9
print(b)
print(type(c))
print(type(b))

#data type => int, float, string, boolean
a=10+7j
print(a)
print(type(a))
print("======================================")
name="Viral"
Number=10
print(name,Number)
print(name+ " " +str(Number))
print("Name: "+name+"\nNamber: "+str(Number))
print(f"Name:{name},Number:{Number}")
print("Name:{},Number:{}".format(name,Number))
print("Name:{0},Number:{1}".format(name,Number))
print("Name:{1},Number:{0}".format(name,Number))
print("Name:{a},Number:{b}".format(a=name,b=Number))
print("Name:%s,Number:%d"%(name,Number))


for i in range(128):
    print(f"ASCII value of {i}: {chr(i)}")